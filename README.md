# Wakeup Bot 

Use AI to create admirable images to surprise your every morning.

<video src="https://github.com/godruoyi/godruoyi/assets/16079222/86732368-adee-407a-958d-94a171d7bc92"></video>

## Features

- [x] 🌰 Support multiple image generators, Bing(DALL E3), OpenAI(E2, E3), Baidu.
- [x] 🍏 Support multiple notification channels, Telegram, Slack.
- [x] 🐛 GitHub Action
- [x] 🐕‍🦺 Support deploy to fly.io
- [x] 🦉 Customizable message format
- [ ] 🦟 Auto save logs to GitHub issues
- [ ] 🐜 Capture output in GitHub Action

## Basic Usage

```yaml
name: wakeuppppp

on:
  workflow_dispatch:

jobs:
  wakeup:
    name: wakeup bot
    runs-on: ubuntu-latest
    steps:
      - name: Wakeup
        uses: godruoyi/wekeup@main
        with:
          tg_token: ${{ secrets.TG_TOKEN }}
          tg_chat_id: ${{ secrets.TG_CHAT_ID }}
          weather_city: "chongqing"
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
```

## Full Example

```yaml
name: wakeuppppp

on:
  workflow_dispatch:

jobs:
  wakeup:
    name: wakeup bot
    runs-on: ubuntu-latest
    steps:
      - name: Wakeup
        uses: godruoyi/wekeup@main
        with:
          # image generator, support [bing_ball_e3, openai, baidu]
          # use comma to split multiple
          drivers: "bing_ball_e3"

          # send message to channels, support [slack, tg]
          channels: "slack"

          # weather city
          weather_city: "chongqing"

          # telegram bot config required when use tg channel
          tg_token: ${{ secrets.TG_TOKEN }}
          tg_chat_id: ${{ secrets.TG_CHAT_ID }}

          # slack config required when use Slack channel
          slack_token: ${{ secrets.SLACK_TOKEN }}
          slack_chat_id: "C0616U4LYHZ"

          # openai azure api config
          # if you use openai api, only need to set openai_api_key
          openai_api_base: "https://godruoyi-openai-azure.openai.azure.com/"
          openai_api_type: "azure"
          openai_api_version: "2023-06-01-preview"
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}

          # bing auth token config required when use bing_ball_e3 driver
          # bing_auth_token: bing cookie that name is "_U"
          # bing_auth_token_kiev: bing cookie that name is "KievRPSAuth"
          bing_auth_token: ${{ secrets.BING_AUTH_TOKEN }}
          bing_auth_token_kiev: ${{ secrets.BING_AUTH_TOKEN_KIEV }}

          # baidu config required when use baidu qianfan driver
          # https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Klkqubb9w#%E9%94%99%E8%AF%AF%E7%A0%81
          qianfan_ak: ${{ secrets.QIANFAN_AK }}
          qianfan_sk: ${{ secrets.QIANFAN_SK }}

          # send error message when occur error
          send_error: "true"

          # message format, available variables:
          # {weather} - weather
          # {sentence} - today's sentence
          # {get_up_time} - get up time
          # {error} - error message
          # {driver} - generator driver, e.g. openai, bing_ball_e3
          # {channel} - notification channel, e.g. tg, telegram, slack
          message_format: "今天的天气: {weather}, 起床时间: {get_up_time}\r\n\r\n起床啦，今天又是充满活力的一天，赶紧起来换尿布吧。\r\n\r\n今日诗句: {sentence}\r\n\r\nPowered by {driver}"
          error_message_format: "今天的天气: {weather}, 起床时间: {get_up_time}\r\n\r\n起床啦，虽然图片生成失败了，但今天依然是充满活力的一天，。\r\n\r\n今日诗句: {sentence}\r\n\r\n生成图片失败: {error} Driver: {driver}"
```


## How to configurate

### Drivers

#### Bing Driver

1. Vist https://bing.com/create and login your Microsoft account(recommend to use GitHub login).
2. Open the browser's developer tools and copy the cookie value of `_U` and `KievRPSAuth`.
3. Set the cookie value to GitHub Secrets, the name is `BING_AUTH_TOKEN` and `BING_AUTH_TOKEN_KIEV`.

#### OpenAI Driver

1. Get OpenAI API Key from OpenAI dashboard.
2. Set the API Key to GitHub Secrets, the name is `OPENAI_API_KEY`.

You can also use Azure API, here are the example:

```yaml
OPENAI_API_BASE: "https://godruoyi-openai-azure.openai.azure.com/" # change to your azure api base url
OPENAI_API_TYPE: "azure"
OPENAI_API_VERSION: "2023-06-01-preview"
OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

#### Baidu Driver

1. Get Baidu Qianfan API Key from [Baidu Qianfan dashboard](https://console.bce.baidu.com/qianfan/overview?_=1699757838186).
2. Create a new application and make sure you have enabled the `Stable-Diffusion-XL` model. 
3. Set the API Key to GitHub Secrets, the `QIANFAN_AK` is your API Key, the `QIANFAN_SK` is your Secret Key.

### Channels

#### Telegram

1. Create a new bot with [BotFather](https://t.me/botfather).
2. Get the bot token and set it to GitHub Secrets, the name is `TG_TOKEN`.
3. Create a new channel and invite the bot to the channel as an administrator.
4. Copy the channel id and set it to GitHub Secrets, the name is `TG_CHAT_ID`.
5. If you don't know how to get the channel id, try to send anything to the JsonDumpBot, it will return the channel id.
6. The chat id should be start with `-100`, like `-1002002109011`.


#### Slack

1. Create a new Slack App with [Slack App](https://api.slack.com/apps).
2. Go to the `OAuth & Permissions` page and get the `Bot User OAuth Token`, set it to GitHub Secrets, the name is `SLACK_TOKEN`.
3. Go to the `OAuth & Permissions` scope page and add the `chat:write, files:write` scope.
4. Install the app to your workspace.
5. Create a new channel and copy the channel id, set it to GitHub Secrets, the name is `SLACK_CHAT_ID`.
6. It should be started with `C`, like `C0616U4LYHZ`.

### Deploy

#### Deploy to fly.io

> Only support telegram channel now, when you finish the deployed, you should set the telegram bot webhook url to fly.io.

1. Create your fly.io account and install flyctl.
2. Clone this repository
3. Set the necessary environment variables using `flyctl secrets set` command.
4. Run `flyctl deploy` to deploy.
5. Get the deployed url and set it to your telegram bot webhook url.

you can use the following command to set the telegram bot webhook url:

```bash
# replace {TG_TOKEN} with your telegram bot token
# change the url to your deployed url
curl https://api.telegram.org/bot{TG_TOKEN}/setWebhook?url=https://boootx.fly.dev/webhooks/tg

# verify the webhook url
curl https://api.telegram.org/bot{TG_TOKEN}/getWebhookInfo
```

now try to send a message that start with `/prompt your prompt or anythong` to your bot, it should return an image.

available prompt:

- /prompt
- /prompt_baidu
- /prompt_dall_e2

see demo here: https://t.me/+9F-S1b2qyWEwYTU1

## How to trigger

1. Install this GitHub Action in your repository, recommend to use your profile repository(such as [godruoyi/wakeup.yml](https://github.com/godruoyi/godruoyi/blob/master/.github/workflows/wakeup.yml)).
2. Create a GitHub Token
3. Install this [Shortcuts](https://www.icloud.com/shortcuts/12071c4bfcbc4fc090ace637c8e43c84) on your iPhone and set your GitHub Token in the shortcut Dictionary.
4. Run it anytime, anywhere.

You can also use CURL to trigger this action, for example:

```bash
curl -X POST "https://api.github.com/repos/godruoyi/godruoyi/actions/workflows/wakeup.yml/dispatches" \
  --header 'Content-Type: application/json' \
  --header 'Authorization: token {GITHUB_TOKEN}' \
  --data '{"ref": "master"}'
```

## Thanks

- @yihong0618
- @BennyThink
- @xenv


## Appreciation

- Thank you, that's enough. Just enjoy it.
