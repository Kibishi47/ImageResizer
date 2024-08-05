import os

class ImagePathCollector:
    def __init__(self):
        pass

    @staticmethod
    def get_image_paths(root_dir):
        image_paths = []
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_paths.append(os.path.join(subdir, file))
        return image_paths