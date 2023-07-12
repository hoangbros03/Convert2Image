import logging
import shutil
from pathlib import Path

from PIL import Image

from handler import Handler

logging.basicConfig(
    filemode="a",
    filename="log.log",
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)


class PNG_Handler(Handler):
    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".png"

    def save(self, original, target):
        shutil.copyfile(original, target)

    def forward(self, file_path, output_dir):
        self.checkDir(output_dir)
        target = (
            Path(".")
            / output_dir
            / str(Path(file_path).stem + Handler.DEFAULT_EXTENSION)
        )
        self.save(file_path, target)


if __name__ == "__main__":
    c = PNG_Handler()
    c.forward("test.png", "outputdir")
