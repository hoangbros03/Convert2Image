import os
from pathlib import Path

import pillow_heif
from PIL import Image

from handler import Handler


class HeicHandler(Handler):
    """
    class of Heic handler
    """

    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".heic"

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
        super().__init__()

    def convert(self, file_path, output_dir):
        """
        Convert function
        Parameters
        ----------
        file_path: Directory of file need to be converted
        output_dir: Name of folder holding output file
        Returns
        -------
        Tuple of the object holding images and list of images information
        """
        heif_file = pillow_heif.read_heif(file_path)
        data = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )
        new_name = file_path.split("\\")[-1]
        new_name = new_name.replace("heic", "png")

        new_name = new_name.replace("HEIC", "png")
        print("New name: ", new_name)
        new_filepath = os.path.join(output_dir, new_name)
        data.save(new_filepath, format("png"))

    def forward(self, file_path, output_dir):
        """
        Function that combines the step
        Parameters
        ----------
        file_path: Directory of file need to be converted
        output_dir: Name of folder holding output file
        Returns
        -------
        Nothing.
        """
        self.convert(file_path, output_dir)
