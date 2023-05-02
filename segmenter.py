from PIL import Image
from transformers import pipeline
import torch

class Segmenter:
    def __init__(self) -> None:
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.segmenter = pipeline(model="nvidia/segformer-b0-finetuned-ade-512-512", device=self.device)
    
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