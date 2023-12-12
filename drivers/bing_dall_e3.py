from http.cookies import SimpleCookie

from BingImageCreator import ImageGen, HEADERS
from fake_useragent import UserAgent

from .driver import Driver
from environment import Environment
from requests.utils import cookiejar_from_dict

ua = UserAgent(browsers=["edge"])


class BingDallE3Driver(Driver):
    auth_token: str = Environment.get_bing_auth_token()
    auth_token_kiev: str = Environment.get_bing_auth_token_kiev()
    cookies: str = Environment.get_bing_cookies()

    def __init__(self):
        if (self.auth_token is None or self.auth_token == "") and (self.cookies is None or self.cookies == ""):
            raise ValueError("BING_AUTH_TOKEN or BING_COOKIES env variable are not set")
        pass

    def generate_images(self, text: str):
        if self.cookies is not None and self.cookies != "":
            return self.generate_images_with_all_cookies(text)
        else:
            return self.generate_images_with_kiev(text)

    def generate_images_with_kiev(self, text: str):
        all_cookies = []
        if self.auth_token_kiev is not None and self.auth_token_kiev != "":
            print("using kiev cookie")
            all_cookies = [{"name": "KievRPSSecAuth", "value": self.auth_token_kiev}]

        i = ImageGen(auth_cookie=self.auth_token, all_cookies=all_cookies)

        return self._generate_images(self, i, text)

    def generate_images_with_all_cookies(self, text: str):
        return self._generate_images(self, self.create_image_generator(), text)

    @staticmethod
    def _generate_images(self, i: ImageGen, text: str):
        try:
            images = i.get_images(text)
            datas = []
            for image in images:
                print("downloading image: ", image)

                # skip image if it's end with .svg
                if image.endswith(".svg"):
                    print("skipping svg image", image)
                    continue

                response = i.session.get(image)
                if response.status_code != 200:
                    print("error downloading image", image, response.status_code)
                    continue
                datas.append(response.content)
            return datas
        except Exception as e:
            raise ValueError(f'error getting images {e}')

    def create_image_generator(self):
        i = ImageGen(auth_cookie="")

        i.session.headers = self.reset_headers()
        i.session.cookies = self.parse_cookie_string(self.cookies)

        return i

    @staticmethod
    def parse_cookie_string(cookie_string):
        cookie = SimpleCookie()
        cookie.load(cookie_string)
        cookies_dict = {}
        cookiejar = None
        for key, morsel in cookie.items():
            if key == "USRLOC":
                continue
            cookies_dict[key] = morsel.value
            cookiejar = cookiejar_from_dict(
                cookies_dict, cookiejar=None, overwrite=True
            )
        return cookiejar

    @staticmethod
    def reset_headers():
        headers = HEADERS
        headers["user-agent"] = ua.random

        return headers
