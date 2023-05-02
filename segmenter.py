from PIL import Image
from transformers import pipeline
from ascii_creator import grayscale_to_ascii

class Segmenter:
    def __init__(self) -> None:
        self.segmenter = pipeline(model="nvidia/segformer-b0-finetuned-ade-512-512")
    
    def get_segment_mask(self, image: Image, class_name: str) -> Image:
        """Returns a mask of the specified class in the image.

        Args:
            image (Image): The regular image.
            class_name (str): The name of the class to get the mask of.

        Returns:
            Image: The mask of the specified class in the image.
        """
        segments = self.segmenter(image)
        for segment in segments:
            if segment['label'] == class_name:
                return segment['mask']
        return None

if __name__ == '__main__':
    segmenter = Segmenter()
    IMAGE_PATH = 'person.jpg'
    image = Image.open(IMAGE_PATH)
    mask = segmenter.get_segment_mask(image, 'person')
    
    # Convert the image to grayscale
    image = image.convert('L')

    # Apply the mask to the image
    masked_image = Image.composite(image, Image.new('L', image.size, 'black'), mask)

    ascii_image = grayscale_to_ascii(masked_image, True)
    with open('ascii_person.txt', 'w') as file:
        file.write(ascii_image)