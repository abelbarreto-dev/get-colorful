from src.model.picture import Picture


class Facade:
    """Project Facade Class to access back-end.
    """

    def __init__(self) -> None:
        """New Facade.
        """
        pass

    def swap_picture_url(self, picture: Picture) -> bool:
        """This function takes a grey scale picture url and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            bool: True if it be a success else False.
        """
        pass

    def swap_picture_local(self, picture: Picture) -> bool:
        """This function takes a grey scale picture local file and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            bool: True if it be a success else False.
        """
        pass
