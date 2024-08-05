from abc import ABC, abstractmethod
from PIL import Image

class ResizeStrategy(ABC):
    @abstractmethod
    def resize(self, image: Image.Image, width: int = None, height: int = None) -> Image.Image:
        pass

class ProportionalResizeStrategy(ResizeStrategy):
    def resize(self, image: Image.Image, width: int = None, height: int = None) -> Image.Image:
        original_width, original_height = image.size
        
        if width and not height:
            height = int((width / original_width) * original_height)
        elif height and not width:
            width = int((height / original_height) * original_width)
        elif width and height:
            aspect_ratio = original_width / original_height
            if (width / height) > aspect_ratio:
                width = int(height * aspect_ratio)
            else:
                height = int(width / aspect_ratio)
        else:
            raise ValueError("Either width or height must be provided when resizing proportionally.")
        
        return image.resize((width, height), Image.Resampling.LANCZOS)

class NonProportionalResizeStrategy(ResizeStrategy):
    def resize(self, image: Image.Image, width: int, height: int) -> Image.Image:
        if not width or not height:
            raise ValueError("Both width and height must be provided when resizing non-proportionally.")
        
        return image.resize((width, height), Image.Resampling.LANCZOS)