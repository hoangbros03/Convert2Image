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
    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".pdf"

    def __init__(self):
        super().__init__()

    def __read(self, file_path):
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

    def convert(self, file_path, output_dir):
        pdfFile, pageNums, imgList = self.__read(file_path)
        self.checkDir(output_dir)
        return pdfFile, imgList

    def save(self, pdfFile, imgList, output_dir):
        for idx, img in enumerate(imgList, start=1):
            # Get image
            baseImg = pdfFile.extract_image(img[0])
            imgBytes = baseImg["image"]

            # Get image new name
            imgName = "Image" + str(idx) + "." + "png"

            # Save the images
            with open(os.path.join(output_dir, imgName), "wb") as img_file:
                img_file.write(imgBytes)

    def forward(self, file_path, output_dir):
        check = self.check_extension(file_path)
        if not check:
            print("WTF?")
        pdf_file, img_list = self.convert(file_path, output_dir)
        self.save(pdf_file, img_list, output_dir)


class PDF_Handler(Handler):
    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".pdf"

    def __init__(self):
        super().__init__()

    def __read(self, file_path):
        return convert_from_path(file_path)

    def convert(self, file_path, output_dir):
        images_from_path = self.__read(file_path)
        check_dir(output_dir)
        return images_from_path

    def forward(self, file_path, output_dir):
        check = self.check_extension(file_path)
        print(Path(file_path).suffix)
        if not check:
            print("WTF?")

        images = self.convert(file_path, output_dir)
        for i in range(len(images)):
            self.save(images[i], Path(file_path).stem + str(i), output_dir)


def convertPDFToImage(file_path: str, output_dir: str, img_only: bool = False) -> None:
    """
    Convert PDF to image function
    Parameters
    ----------
    Nothing
    Returns
    -------
    Nothing
    """
    if img_only:
        pdfFile = fitz.open(file_path)
        pageNums = len(pdfFile)
        logging.info(f"page has {pageNums} image(s)")
        # Init list of images
        imgList = []

        for i in range(pageNums):
            imgList.extend(pdfFile[i].get_images())

        if len(imgList) == 0:
            logging.error("No images found in the provided pdf file")

        check_dir(output_dir)

        for idx, img in enumerate(imgList, start=1):
            # Get image
            baseImg = pdfFile.extract_image(img[0])
            imgBytes = baseImg["image"]

            # Get image new name
            imgName = "Image" + str(idx) + "." + "png"

            # Save the images
            with open(os.path.join(output_dir, imgName), "wb") as img_file:
                img_file.write(imgBytes)
    else:
        check_dir(output_dir)
        images_from_path = convert_from_path(file_path)

        for i in range(len(images_from_path)):
            images_from_path[i].save(
                os.path.join(output_dir, "Image" + str(i) + ".png"), "PNG"
            )


def check_dir(output_dir):
    # Check if dir exist, otherwise create new
    """
    abc.
    """
    if not os.path.exists(output_dir):
        logging.info("Output dir doesn't exist. Creating...")
        os.mkdir(output_dir)
        logging.info("Output dir created.")
