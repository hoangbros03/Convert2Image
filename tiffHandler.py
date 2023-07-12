from pathlib import Path
from PIL import Image, ImageSequence

class TiffHandler(Handler):
    SUPPORT_EXTENSIONS = ".tiff"

    def __init__(self):
        pass

    def __read(self):
        pass

    def convert(self, file_path, output_dir):
        '''
        Convert input file .tiff to .png
        '''
        filename = Path(file_path).name
        try:
            im = Image.open(file_path)
            for i, page in enumerate(ImageSequence.Iterator(im)):
                output_filename = filename + "-" + str(i+1) + ".png"   
                page.save(output_filename)
                    
        except:
            print(Path(file_path).suffix)


