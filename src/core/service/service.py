from src.core.api.api_deepai import APIDeepAI
from src.model.picture import Picture


class Service:
    """It is the service of application, here data is checked
    and if success, it try to make download from wished file.
    """

    def __init__(self) -> None:
        """New Service.
        """
        self._deepai = APIDeepAI()

    @property
    def deepai(self) -> APIDeepAI:
        return self._deepai

    def swap_picture_url(self, picture: Picture) -> bool:
        """This function takes a grey scale picture url and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            bool: True if it be a success else False.
        """
        if not self._check_data_picture(picture=picture):
            return False

    def swap_picture_local(self, picture: Picture) -> bool:
        """This function takes a grey scale picture local file and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            bool: True if it be a success else False.
        """
        if not self._check_data_picture(picture=picture):
            return False

    def _check_data_picture(self, picture: Picture) -> bool:
        """This method makes validation data from picture.
        It checks if online or local, no matter.

        Args:
            picture (Picture): instance of Picture.

        Returns:
            bool: True if success else False.
        """
        return False
