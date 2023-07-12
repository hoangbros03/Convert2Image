from pathlib import Path

from PIL import Image, ImageSequence

from handler import Handler


class TiffHandler(Handler):
    """
    Tiff handler class.
    """

    SUPPORT_EXTENSIONS = ".tiff"

    def convert(self, file_path: Path, output_dir: Path) -> None:
        """
        Convert function
        Parameters
        ----------
        file_path: Directory of file need to be converted
        output_dir: Name of folder holding output file
        Returns
        -------
        Nothing.
        """
        # filename = Path(file_path).name
        filename = Path(file_path)
        try:
            im = Image.open(file_path)
            for i, page in enumerate(ImageSequence.Iterator(im)):
                if output_dir is not None:
                    output_filename = Path(output_dir) / str(
                        filename.name + "-" + str(i + 1) + Handler.DEFAULT_EXTENSION
                    )
                else:
                    output_filename = str(
                        filename.name + "-" + str(i + 1) + Handler.DEFAULT_EXTENSION
                    )
                page.save(output_filename)

        except FileNotFoundError:
            print(f"Exception while handling file {file_path}")

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
        self.convert(Path(file_path), output_dir)
