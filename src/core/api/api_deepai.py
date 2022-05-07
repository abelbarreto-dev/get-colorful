import json
from requests import post as deep_ai


class APIDeepAI:
    """This class has the function to just make
    requests from an extern API.
    """

    # API URL
    URLAPI = 'https://api.deepai.org/api/colorizer'

    def __init__(self) -> None:
        """New APIDeepAI.
        """
        pass

    def picture_url(self, pict_url: str) -> json:
        """This mathod takes an image from internet,
        grey scale and transform it.

        Args:
            pict_url (str): url to image.

        Returns:
            json: a json with file required output.
        """
        response = deep_ai(
            self.URLAPI,
            data={
                'image': pict_url,
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        return response.json()

    def picture_local(self, pict_path: str) -> json:
        """This mathod takes an image from a local storage,
        grey scale and transform it.

        Args:
            pict_path (str): path to image.

        Returns:
            json: a json with file required output.
        """
        response = deep_ai(
            self.URLAPI,
            files={
                'image': open(pict_path, 'rb'),
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        return response.json()
