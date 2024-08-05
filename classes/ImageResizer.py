from classes.ResizeStrategy import *
from classes.ImagePathCollector import ImagePathCollector
import os

class ImageResizer:
    def __init__(self):
        pass
    
    @classmethod
    def resize_current(cls, input_dir: str = "./ressources/src", width: int = None, height: int = None, width_mm: float = None, height_mm: float = None, proportional: bool = True, dpi: int = 300, landscape: bool = False):
        image_paths = ImagePathCollector.get_image_paths(input_dir)
        output_dir = f"{input_dir}{"/" if not input_dir.endswith("/") else ""}result"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Le dossier de sortie {output_dir} a été créé.")
        for image_path in image_paths:
            try:
                # Détermine le chemin de sortie
                output_path = os.path.join(output_dir, os.path.basename(image_path))

                cls.__resize(image_path, output_path, width, height, width_mm, height_mm, proportional, dpi, landscape)
                
                print(f"Image redimensionnée : {output_path}")
            
            except Exception as e:
                print(f"Erreur lors du traitement de l'image {image_path} : {e}")

    @classmethod
    def resize_path(cls, input_path: str, output_path: str = "result.png", width: int = None, height: int = None, width_mm: float = None, height_mm: float = None, proportional: bool = True, dpi: int = 300, landscape: bool = False):
        cls.__resize(input_path, output_path, width, height, width_mm, height_mm, proportional, dpi, landscape)

    @classmethod
    def __resize(cls, input_path: str, output_path: str, width: float, height: float, width_mm: float, height_mm: float, proportional: bool, dpi: int, landscape: bool):
        strategy = ProportionalResizeStrategy() if proportional else NonProportionalResizeStrategy()
        image = Image.open(input_path)

        original_width, original_height = image.size
        if landscape and original_height > original_width:
            image = image.rotate(90, expand=True)
        elif not landscape and original_width > original_height:
            image = image.rotate(90, expand=True)

        width = width if width else (cls.__get_pixels_value(width_mm, dpi) if width_mm else None)
        height = height if height else (cls.__get_pixels_value(height_mm, dpi) if height_mm else None)
        resized_image = strategy.resize(image, width, height)
        resized_image.save(output_path, dpi=(dpi, dpi))

    @classmethod
    def __get_pixels_value(clas, value, dpi: int):
        return int((value * dpi) / 25.4)