from src.core.api.api_deepai import APIDeepAI
from src.model.picture import Picture
from src.core.singleton.sing_message import SingMessage as SMG
from src.core.utils.utils import (
    instanceok, isdirect, isitfile, isiturl, get_name
)


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
        # cleaning message
        SMG.message().clear_msg()
        # checks if instance is Picture, if it isn't, return False
        if not instanceok(picture=Picture):
            SMG.message().warning = True
            SMG.message().title = 'Warning - Invalid Instance'
            SMG.message().text = 'Warning! Instance must be Picture'
            return False
        # instance ok ## check if saving directory is valid, else return False
        if not isdirect(picture.save):
            SMG.message().warning = True
            SMG.message().title = 'Warning - Invalid Directory'
            SMG.message().text = 'Warning! Directory Invalid to Save'
            return False
        # save directory ok ## if it is not a local or online file
        if not picture.online:
            if not isitfile(file=picture.source):
                SMG.message().warning = True
                SMG.message().title = 'Warning - Local File'
                SMG.message().text = 'Warning! Local File Not Found'
                return False
        else:
            if not isiturl(url=picture.source):
                SMG.message().warning = True
                SMG.message().title = 'Warning - Online File'
                SMG.message().text = 'Warning! URL File Not Found'
                return False
        # file path (local or online) ok ## if user don't put on name
        # inserts it ### success
        if not picture.name:
            picture.name = get_name(wordpath=picture.source)
        # if came here, it represents a success operation
        return True
