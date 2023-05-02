from PIL import Image

def grayscale_to_ascii(image: Image, white_text=False) -> str:
    """Converts a grayscale image to an ASCII representation.

    Args:
        image (Image): A grayscale image.
        white_text (bool, optional): Whether to use white text on a black background. Defaults to False.

    Returns:
        str: An ASCII representation of the image.
    """
    ascii_chars = """@%#*+=-:. """
    if white_text:
        ascii_chars = ascii_chars[::-1]
    ascii_image = ''
    pixels = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            ascii_image += ascii_chars[int(pixels[x, y] / 256 * len(ascii_chars))]
        ascii_image += '\n'
    return ascii_image