import re

from fastapi import FastAPI, Request
from drivers import make_image_driver, DRIVER_DALL_E3, DRIVER_DALL_E2, DRIVER_BAIDU
from environment import Environment
from telebot import TeleBot, types

app = FastAPI()
bot = TeleBot(Environment.get_tg_token())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.api_route("/webhooks/tg", methods=["POST"])
async def webhook_tg(req: Request):
    body = await req.body()
    decoded = body.decode("utf-8")

    return bot.process_new_updates([types.Update.de_json(decoded)])


@bot.message_handler(commands=['promote', 'promote_dall_e3'])
def process_tg_dall_e3(message):
    print("promote dall e3")
    return process(message, DRIVER_DALL_E3)


@bot.message_handler(commands=['promote_dall_e2'])
def process_tg_dall_e2(message):
    print("promote dall e2")
    return process(message, DRIVER_DALL_E2)


@bot.message_handler(commands=['promote_baidu'])
def process_tg_baidu(message):
    print("promote baidu")
    return process(message, DRIVER_BAIDU)


def process(message, driver):
    promote = re.sub(r'^/promote[\w\d_-]*', '', message.text).strip()
    if promote == "":
        bot.reply_to(message, "please input your promote")
        return

    print(f"Start generating images for `{promote}` with driver {driver}, please wait...")
    bot.reply_to(message, f"Start generating images with driver {driver}, please wait...")

    try:
        images = make_image_driver(driver).generate_images(promote)
    except Exception as e:
        print("error generating images: ", e)

        bot.reply_to(message, f"generate images failed: {e}")
        return

    media = [types.InputMediaPhoto(image) for image in images]
    bot.send_media_group(
        reply_to_message_id=message.message_id,
        chat_id=message.chat.id,
        media=media,
        disable_notification=True,
    )

    return {"message": "done"}
