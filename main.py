import argparse

from handler import Handler
from heic_to_png import HeicHandler
from pdfHandler import PDF_Handler
from pngHandler import PNG_Handler
from tiffHandler import TiffHandler


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
    elif TiffHandler.check_extension(cls=TiffHandler, filename=file_name):
        return TiffHandler()
    elif HeicHandler.check_extension(cls=HeicHandler, filename=file_name):
        # PNG handler because heic handler have some ??? problems
        return PNG_Handler()
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


def main():
    """Convert file from argument to image
    Return: A path to a folder containing that image?
    """
    parse = parse_args()
    model = getModel(parse.image_file[0])
    model.forward(parse.image_file[0], parse.output_dir)


if __name__ == "__main__":
    main()
