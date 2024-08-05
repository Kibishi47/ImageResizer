# Image Resizer with Automatic Orientation

This project is an image resizing tool that lets you resize images by specifying dimensions in millimetres or pixels. It automatically manages the orientation of images to adjust them in landscape or portrait mode as required.

## Features

- Proportional or non-proportional resizing of images by specifying dimensions in millimetres.
- Supports automatic image orientation (landscape or portrait).
- Ability to process an entire folder and its sub-folders to resize all images.
- Automatic management of output folder creation if none exists.

## Prerequisites

- Python 3.x
- [Pillow](https://python-pillow.org/): Python library for image processing.

## Installation

1. **Run the repository :**

   bash
   git clone [https://github.com/Kibishi47/image-resizer.git](https://github.com/Kibishi47/ImageResizer.git)
   cd ImageResizer
   ```

2. **Install dependencies:**

   ```bash
   pip install pillow
   ```

## Usage

### Sample script

You can use the Python script provided to resize images in a folder and its subfolders.

python
from your_module_name import ImageProcessor, ProportionalResizeStrategy, ImagePathCollector

root_dir = 'path_to_image_folder
output_dir = 'path_to_output_folder
strategy = ProportionalResizeStrategy()

# Retrieve image paths
collector = ImagePathCollector(root_dir)
image_paths = collector.get_image_paths()

# Process images specifying width in millimetres and landscape orientation
processor = ImageProcessor(strategy)
processor.process_images(image_paths, output_dir, width_mm=63, dpi=96, landscape=True)
```

### Options

- **width_mm** : Largeur souhaitée en millimètres.
- **height_mm** : Hauteur souhaitée en millimètres.
- **dpi** : Dots Per Inch (DPI) pour la conversion des dimensions en pixels. Par défaut à 96.
- **landscape** : Si `True`, oriente les images en paysage. Si `False`, oriente les images en portrait.

## Structure du projet

```
image-resizer/
│
├── your_module_name/
│   ├── __init__.py
│   ├── image_processor.py  # Contient les classes ImageProcessor, ImageResizer, etc.
│   ├── resize_strategies.py # Contient les classes ProportionalResizeStrategy, NonProportionalResizeStrategy
│   └── image_path_collector.py # Contient la classe ImagePathCollector
│
├── README.md
└── requirements.txt
```

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour proposer des améliorations ou signaler des bugs.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
