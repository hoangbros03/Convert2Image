import argparse

from handler.handler import Handler
from handler.heicHandler import Heic_Handler
from handler.pdfHandler import PDF_Handler
from handler.pngHandler import PNG_Handler
from handler.tiffHandler import Tiff_Handler


def getModel(file_name: str) -> Handler:
    """
    Function to get model
    Parameters
    ----------
    file_name: Name of the file
    Returns
    -------
    Model that is suitable to get png image
    """
    if PDF_Handler.check_extension(cls=PDF_Handler, filename=file_name):
        return PDF_Handler()
    elif PNG_Handler.check_extension(cls=PNG_Handler, filename=file_name):
        return PNG_Handler()
    elif Tiff_Handler.check_extension(cls=Tiff_Handler, filename=file_name):
        return Tiff_Handler()
    elif Heic_Handler.check_extension(cls=Heic_Handler, filename=file_name):
        return Heic_Handler()
    else:
        raise ValueError("Unsupported file format")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Convert file to image")
    parser.add_argument(
        "-f",
        "--image_file",
        type=str,
        nargs="+",
        help="Insert image file that need converting to png",
    )  # image path argument
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="outputFiles",
        help="Folder that holds converted image(s)",
    )  # image path argument
    return parser.parse_args()
