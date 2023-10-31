# Wakeup Bot 

Use AI to create admirable images to surprise your every morning.

<video src="https://github.com/godruoyi/godruoyi/assets/16079222/86732368-adee-407a-958d-94a171d7bc92"></video>

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

## How to trigger

1. Install this GitHub Action in your repository, recommend to use your profile repository(such as [godruoyi/wakeup.yml](https://github.com/godruoyi/godruoyi/blob/master/.github/workflows/wakeup.yml)).
2. Create a GitHub Token
3. Install this Shortcuts on your iPhone and set your GitHub Token in the shortcut Dictionary.
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
