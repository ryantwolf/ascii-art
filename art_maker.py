from ascii_creator import grayscale_to_ascii
from segmenter import Segmenter
from PIL import Image
import argparse

class AsciiArtMaker:
    def __init__(self) -> None:
        self.segmenter = Segmenter()
    
    def make_ascii(self, image_path: str, output_path: str, white_text=False):
        """Makes an ASCII art representation of the people in an image.

        Args:
            image_path (str): The path to the image.
            output_path (str): The path to save the ASCII art to.
            white_text (bool, optional): Whether to use white text on a black background. Defaults to False.
        """
        image = Image.open(image_path)
        mask = self.segmenter.get_segment_mask(image, 'person')
        
        # Convert the image to grayscale
        image = image.convert('L')

        # Apply the mask to the image
        masked_image = Image.composite(image, Image.new('L', image.size, 'black'), mask)

        ascii_image = grayscale_to_ascii(masked_image, white_text)
        with open(output_path, 'w') as file:
            file.write(ascii_image)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Makes an ASCII art representation of the people in an image.')
    parser.add_argument('image_path', type=str, help='The path to the image.')
    parser.add_argument('output_path', type=str, help='The path to save the ASCII art to.')
    parser.add_argument('--white_text', action='store_true', help='Whether to use white text on a black background.')
    args = parser.parse_args()

    maker = AsciiArtMaker()
    maker.make_ascii(args.image_path, args.output_path, args.white_text)