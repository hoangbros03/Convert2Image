import os
from pathlib import Path

from PIL import Image


class Handler:
    """
    Handler class
    """

    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = None

    def __init__(self):
        """
        Constructor of the class
        Parameters
        ----------
        Nothing
        Returns
        -------
        Nothing
        """
        pass

    def check_extension(cls, filename):
        """
        Check extension of the file
        Parameters
        ----------
        filename: name of the file
        Returns
        -------
        Boolean value indicate if it's ok or not.
        """
        ext = Path(filename).suffix
        return ext == cls.SUPPORT_EXTENSIONS

    def __read(self):
        """
        Read file function
        Parameters
        ----------
        Nothing
        Returns
        -------
        Nothing
        """
        pass

    def convert(self, file_path, output_dir):
        """
        Convert to PIL image
        Parameters
        ----------
        file_path: path of the file
        output_dir: Folder name whose contains output images
        Returns
        -------
        Nothing
        """
        pass

    def checkDir(self, output_dir):
        """
        Check if folder is existed
        Parameters
        ----------
        output_dir: name of the folder
        Returns
        -------
        Nothing
        """
        # Check if dir exist, otherwise create new
        if output_dir is None:
            return
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

    def forward(self, file_path, output_dir):
        """
        Function that excecute from A-Z
        Parameters
        ----------
        file_path: path of the file
        output_dir: Folder name whose contains output images
        Returns
        -------
        Nothing
        """
        pass

    def save(self, img: Image, prefix_name, output_dir):
        """
        Save function.
        Parameters
        ----------
        img: PIL image object
        prefix_name: name of output image
        output_dir: Folder that holds output image(s)
        Returns
        -------
        Nothing
        """
        img.save(Path(".") / output_dir / str(prefix_name + Handler.DEFAULT_EXTENSION))
