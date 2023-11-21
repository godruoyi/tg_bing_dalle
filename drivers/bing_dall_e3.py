from BingImageCreator import ImageGen
from .driver import Driver
from environment import Environment


class BingDallE3Driver(Driver):
    auth_token: str = Environment.get_bing_auth_token()
    auth_token_kiev: str = Environment.get_bing_auth_token_kiev()

    def __init__(self):
        if self.auth_token is None or self.auth_token == "":
            raise ValueError("BING_AUTH_TOKEN env variable not set")
        pass

    def generate_images(self, text: str):
        all_cookies = []
        if self.auth_token_kiev is not None and self.auth_token_kiev != "":
            print("using kiev cookie")
            all_cookies = [{"name": "KievRPSSecAuth", "value": self.auth_token_kiev}]

        i = ImageGen(auth_cookie=self.auth_token, all_cookies=all_cookies)
        try:
            images = i.get_images(text)
            datas = []
            for image in images:
                print("downloading image: ", image)
                response = i.session.get(image)
                if response.status_code != 200:
                    print("error downloading image", image, response.status_code)
                    continue
                datas.append(response.content)
            return datas
        except Exception as e:
            raise ValueError(f'error getting images {e}')
