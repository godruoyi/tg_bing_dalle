import io
import random
import qianfan

from .driver import Driver
from environment import Environment


class BaiduDriver(Driver):
    qfg = None

    def __init__(self):
        ak = Environment.get_qianfan_ak()
        sk = Environment.get_qianfan_sk()
        if ak is None or ak == "":
            raise ValueError("QIANFAN_AK env variable not set")
        if sk is None or sk == "":
            raise ValueError("QIANFAN_SK env variable not set")
        qianfan.AK(ak)
        qianfan.SK(sk)
        self.qfg = qianfan.Text2Image()

    def generate_images(self, text: str):
        n = random.randint(2, 4)
        resp = self.qfg.do(prompt=text, with_decode="base64", n=n, size="1024x1024")

        if 'error_code' in resp:
            msg = 'error_msg' in resp and resp['error_msg'] or 'unknown error'
            raise ValueError(f'error generating images {msg}')

        images = []
        for item in resp['data']:
            if 'image' in item:
                images.append(item['image'])

        return images

