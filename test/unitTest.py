import sys
from pathlib import Path

import numpy as np
import targetPaths
from PIL import Image

sys.path.append("../")
from handler.handler import Handler
from utils import getModel


def test(filepaths: Path, outputdir: str) -> None:
    """
    Unit test function.
    Parameters
    ----------
    filepaths: Link to the file need to be converted
    outputdir: Output folder
    Returns
    -------
    None
    """
    # Read, convert, and save images
    model = getModel(Path(filepaths).name)
    extension = model.SUPPORT_EXTENSIONS
    if extension is None:
        raise TypeError("support extension is none.")

    model.forward(Path(filepaths), outputdir)

    # Check if dir exist
    if extension == ".png" or extension == ".heic":
        dest_path = (
            Path(".")
            / outputdir
            / str(Path(filepaths).stem + Handler.DEFAULT_EXTENSION)
        )
        target_path = (
            targetPaths.PNG_TARGET_PATH
            if extension == ".png"
            else targetPaths.HEIC_TARGET_PATH
        )
    else:
        # Check first file of pdf and tiff file(s)
        dest_path = (
            Path(".")
            / outputdir
            / str(
                Path(filepaths).stem
                + Handler.FIRST_FILE_INDICATION
                + Handler.DEFAULT_EXTENSION
            )
        )
        target_path = (
            targetPaths.PDF_TARGET_PATH
            if extension == ".pdf"
            else targetPaths.TIFF_TARGET_PATH
        )

    if not dest_path.exists():
        raise Exception("Can't find output file specified!")

    if not target_path.exists():
        raise Exception("Target file is missing!")

    # Get images
    dest_img = Image.open(dest_path)
    dest_matrix = np.array(dest_img)
    target_img = Image.open(target_path)
    target_matrix = np.array(target_img)

    if len(dest_matrix.shape) != 3:
        raise Exception("Image converted has wrong shape!")

    # Compare two images
    comparison = dest_matrix == target_matrix
    if comparison.all():
        print("Unit test ok!")
    else:
        raise Exception("Two images are different. Test failed.")


if __name__ == "__main__":
    test("inputFiles/untitled-1.pdf", "outputFiles")
