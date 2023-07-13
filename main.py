from utils import getModel, parse_args


def main():
    """Convert file from argument to image
    Return: A path to a folder containing that image?
    """
    parse = parse_args()
    model = getModel(parse.image_file[0])
    model.forward(parse.image_file[0], parse.output_dir)


if __name__ == "__main__":
    main()
