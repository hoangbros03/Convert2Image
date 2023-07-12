import logging
import os
import tempfile
from pathlib import Path

import fitz
from pdf2image import convert_from_path
from PIL import Image

from handler import Handler

logging.basicConfig(
    filemode="a",
    filename="log.log",
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)


class PDF_Image_Handler(Handler):
    """
    PDF Image Handler.
    """

    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".pdf"

    def __init__(self) -> None:
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

    def __read(self, file_path: Path):
        """
        Function that read the file
        Parameters
        ----------
        file_path: Path of the file
        Returns
        -------
        pdfFile, pageNums, imgList
        """
        pdfFile = fitz.open(file_path)
        pageNums = len(pdfFile)
        logging.info(f"page has {pageNums} image(s)")
        # Init list of images
        imgList = []

        for i in range(pageNums):
            imgList.extend(pdfFile[i].get_images())

        if len(imgList) == 0:
            logging.error("No images found in the provided pdf file")

        return pdfFile, pageNums, imgList

    def convert(self, file_path: Path, output_dir: str):
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
        pdfFile, pageNums, imgList = self.__read(file_path)
        self.checkDir(output_dir)
        return pdfFile, imgList

    def save(self, pdfFile: object, imgList: list, output_dir: str) -> None:
        """
        Function to save the file
        Parameters
        ----------
        pdfFile: Object that holds images
        imgList: List of image information
        output_dir: Dir of output folder
        Returns
        -------
        Nothing
        """
        for idx, img in enumerate(imgList, start=1):
            # Get image
            baseImg = pdfFile.extract_image(img[0])
            imgBytes = baseImg["image"]

            # Get image new name
            imgName = "Image" + str(idx) + Handler.DEFAULT_EXTENSION

            # Save the images
            with open(os.path.join(output_dir, imgName), "wb") as img_file:
                img_file.write(imgBytes)

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
        check = self.check_extension(file_path)
        if not check:
            print("WTF?")
        pdf_file, img_list = self.convert(file_path, output_dir)
        self.save(pdf_file, img_list, output_dir)


class PDF_Handler(Handler):
    """
    class handle PDF pages
    """

    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".pdf"

    def __init__(self) -> None:
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

    def __read(self, file_path: Path):
        """
        Function that read the file
        Parameters
        ----------
        file_path: Path of the file
        Returns
        -------
        images from path
        """
        return convert_from_path(file_path)

    def convert(self, file_path: Path, output_dir: str):
        """
        Function that convert the file to list of images
        Parameters
        ----------
        file_path: Path of the file
        output_dir: Name of output folder
        Returns
        -------
        images from path
        """
        self.checkDir(output_dir)
        images_from_path = self.__read(file_path)
        return images_from_path

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
        check = self.check_extension(file_path)
        print(Path(file_path).suffix)
        if not check:
            print("WTF?")

        images = self.convert(file_path, output_dir)
        for i in range(len(images)):
            self.save(images[i], Path(file_path).stem + str(i), output_dir)
