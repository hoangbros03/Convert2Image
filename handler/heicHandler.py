import os
from pathlib import Path

import pillow_heif
from PIL import Image

from handler.handler import Handler


class Heic_Handler(Handler):
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

        self.checkDir(output_dir)
        data.save(
            Path(".")
            / output_dir
            / str(Path(file_path).stem + Handler.DEFAULT_EXTENSION),
            format("png"),
        )

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
