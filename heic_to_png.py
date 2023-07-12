import os
from pathlib import Path

import pillow_heif
from PIL import Image


class Handler:
    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = None

    def __init__(self):
        pass

    def check_extension(cls, filename):
        ext = Path(filename).suffix
        return ext == cls.SUPPORT_EXTENSIONS

    def __read(self):
        pass

    def convert(self, file_path, output_dir):
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
        new_filepath = os.path.join(output_dir, new_name)
        data.save(new_filepath, format("png"))

    def checkDir(self, output_dir):
        # Check if dir exist, otherwise create new
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

    def save(self, img, prefix_name, output_dir):
        img.save(Path(".") / output_dir / prefix_name + Handler.DEFAULT_EXTENSION)


if __name__ == "__main__":
    file_path = r"c:\Users\Tammy\demo\heic-image-converter\test\heic\IMG_1919.HEIC"
    output_dir = r"c:\Users\Tammy\demo\heic-image-converter\test\output"

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
    new_filepath = os.path.join(output_dir, new_name)
    data.save(new_filepath, format("png"))
