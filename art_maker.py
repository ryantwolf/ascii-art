from ascii_creator import grayscale_to_ascii
from segmenter import Segmenter
from PIL import Image

class AsciiArtMaker:
    def __init__(self) -> None:
        self.segmenter = Segmenter()
    
    def make_ascii(self, image_path: str, output_path: str):
        """Makes an ASCII art representation of the image.

        Args:
            image_path (str): The path to the image.
            output_path (str): The path to save the ASCII art to.
        """
        image = Image.open(image_path)
        mask = self.segmenter.get_segment_mask(image, 'person')
        
        # Convert the image to grayscale
        image = image.convert('L')

        # Apply the mask to the image
        masked_image = Image.composite(image, Image.new('L', image.size, 'black'), mask)

        ascii_image = grayscale_to_ascii(masked_image, True)
        with open(output_path, 'w') as file:
            file.write(ascii_image)

if __name__ == '__main__':
    maker = AsciiArtMaker()
    maker.make_ascii('person.jpg', 'ascii_person.txt')