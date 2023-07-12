import argparse


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Convert file to image")
    parser.add_argument(
        "-f",
        "--image-file",
        type=str,
        nargs="+",
        help="Insert image file that need converting to png",
    )  # image path argument
    return parser.parse_args()


def main():
    """Convert file from argument to image
    Return: A path to a folder containing that image?
    """
    pass


if __name__ == "__main__":
    main()
