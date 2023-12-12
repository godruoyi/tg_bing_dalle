import os


class Environment:
    """
    Environment variables:

    DRIVERS - drivers, default: openai, use comma to separate multiple drivers (openai, bing_ball_e3, baidu)

    CITY - get weather for this city, default: chongqing

    # bing dall e3 image engine, not working now
    BING_ALL_COOKIES - Bing Image Create all cookies
    BING_AUTH_TOKEN - Bing Image Search API token - deprecated
    BING_AUTH_TOKEN_KIEV - Bing Image Search API token for Kiev - deprecated

    # openai image engine
    OPENAI_API_BASE - OpenAI API base url, default: https://api.openai.com/v1
    OPENAI_API_TYPE - OpenAI API type, default: open_ai
    OPENAI_API_VERSION - OpenAI API version, default: None
    OPENAI_API_KEY - OpenAI API key
    DALL_MODEL - DALL model, default: dall-e-2, available: dall-e-2, dall-e-3

    CHANNELS - Notification channels, default: tg, use comma to separate multiple channels (tg, slack), will send
        multiple messages if multiple channels are specified

    # telegram channel, required when CHANNELS contains tg
    TG_TOKEN - Telegram bot token
    TG_CHAT_ID - Telegram chat id, required when

    SLACK_TOKEN - Slack bot token
    SLACK_CHAT_ID - Slack chat id

    SEND_ERROR - Send error message to channel, default: false

    # message format, available variables:
    # {weather} - weather
    # {sentence} - today's sentence
    # {get_up_time} - get up time
    # {error} - error message
    # {driver} - generator driver, e.g. openai, bing_ball_e3
    # {channel} - notification channel, e.g. tg, telegram, slack
    MESSAGE_FORMAT - Message format
    ERROR_MESSAGE_FORMAT - Error message format
    """

    @staticmethod
    def get_city():
        return Environment.get_env("CITY", "chongqing")

    @staticmethod
    def get_bing_auth_token():
        return Environment.get_env("BING_AUTH_TOKEN")

    @staticmethod
    def get_bing_cookies():
        return Environment.get_env("BING_ALL_COOKIES")

    @staticmethod
    def get_bing_auth_token_kiev():
        return Environment.get_env("BING_AUTH_TOKEN_KIEV")

    @staticmethod
    def get_openai_api_base():
        return Environment.get_env("OPENAI_API_BASE", "https://api.openai.com/v1")

    @staticmethod
    def get_openai_api_type():
        return Environment.get_env("OPENAI_API_TYPE", "openai")

    @staticmethod
    def get_openai_api_version():
        return Environment.get_env("OPENAI_API_VERSION")

    @staticmethod
    def get_openai_api_key():
        return Environment.get_env("OPENAI_API_KEY")

    @staticmethod
    def get_dall_model():
        return Environment.get_env("DALL_MODEL", "dall-e-2")

    @staticmethod
    def get_tg_token():
        return Environment.get_env("TG_TOKEN")

    @staticmethod
    def get_tg_chat_id():
        return Environment.get_env("TG_CHAT_ID")

    @staticmethod
    def get_channels():
        return Environment.get_env("CHANNELS", "tg").split(",")

    @staticmethod
    def send_error():
        return Environment.get_env("SEND_ERROR", "false") == "true"

    @staticmethod
    def get_message_format():
        default = """今天的天气: {weather}, 起床时间: {get_up_time}

起床啦，今天又是充满活力的一天。

今日诗句: {sentence}

Powered by {driver}"""

        return Environment.get_env("MESSAGE_FORMAT", default)

    @staticmethod
    def get_error_message_format():
        default = """error: : {error}, driver: {driver}"""
        return Environment.get_env("ERROR_MESSAGE_FORMAT", default)

    @staticmethod
    def get_drivers():
        return Environment.get_env("DRIVERS", "openai").split(",")

    @staticmethod
    def get_slack_token():
        return Environment.get_env("SLACK_TOKEN")

    @staticmethod
    def get_slack_chat_id():
        return Environment.get_env("SLACK_CHAT_ID")

    @staticmethod
    def get_qianfan_ak():
        return Environment.get_env("QIANFAN_AK")

    @staticmethod
    def get_qianfan_sk():
        return Environment.get_env("QIANFAN_SK")

    @staticmethod
    def get_env(key: str, default: str = None):
        v = os.getenv(key)
        if v is None or v == "":
            return default
        return v
