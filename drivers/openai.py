import json
import requests
from openai import AzureOpenAI, OpenAI

from .driver import Driver
from environment import Environment


def create_openai_client():
    if Environment.get_openai_api_type() == "azure":
        model = Environment.get_dall_model()
        if model != "dall-e-3":
            # can't deploy dall-e-2 to azure now
            raise ValueError(f'azure only support dall-e-3 model, but got {model}')

        client = AzureOpenAI(
            api_version=Environment.get_openai_api_version(),
            azure_endpoint=Environment.get_openai_api_base(),
            api_key=Environment.get_openai_api_key(),
        )
    else:
        client = OpenAI(
            api_key=Environment.get_openai_api_key(),
        )

    return client


class OpenAIDriver(Driver):
    client: OpenAI = None

    def __init__(self):
        self.client = create_openai_client()

    def generate_images(self, text: str):
        print("using openai {0} model to generate images".format(Environment.get_dall_model()))

        response = self.client.images.generate(
            prompt=text,
            model=Environment.get_dall_model(),
            size='1024x1024',
            n=1,
        )

        results = json.loads(response.model_dump_json())

        print("generate image success, start downloading images...")

        try:
            images = []
            for image in results["data"]:
                print("downloading image: ", image["url"])
                print("revised prompt: ", image["revised_prompt"])

                response = requests.get(image["url"])
                if response.status_code != 200:
                    print("error downloading image", image["url"], response.status_code)
                    continue
                images.append(response.content)
            return images
        except Exception as e:
            raise ValueError(f'error getting images {e}')
