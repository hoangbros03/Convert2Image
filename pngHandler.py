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
    """
    PNG handler class.
    """

    DEFAULT_EXTENSION = ".png"
    SUPPORT_EXTENSIONS = ".png"

    def save(self, original: Path, target: Path) -> None:
        """
        Function to simply save file
        Parameters
        ----------
        original: Original directory of png file
        target: Target directory of target file
        Returns
        -------
        Nothing
        """
        shutil.copyfile(original, target)

    def forward(self, file_path: str, output_dir: str) -> None:
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
        if output_dir is None:
            target = Path(".") / str(Path(file_path).stem + Handler.DEFAULT_EXTENSION)

        else:
            self.checkDir(output_dir)
            target = (
                Path(".")
                / output_dir
                / str(Path(file_path).stem + Handler.DEFAULT_EXTENSION)
            )
        self.save(Path(file_path), target)


if __name__ == "__main__":
    c = PNG_Handler()
    c.forward("test.png", "outputdir")
