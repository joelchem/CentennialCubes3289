from PIL import Image
import os

images = [
    "CentennialCubes_211812.jpg",
    "CentennialCubes_211818.jpg",
    "CentennialCubes_211824.jpg",
    "CentennialCubes_211829.jpg",
    "CentennialCubes_211835.jpg",
    "CentennialCubes_211841.jpg",
    "CentennialCubes_211847.jpg",
    "CentennialCubes_211853.jpg",
    "CentennialCubes_211859.jpg",
]

IMAGE_PATH = "Images/"
dirs = os.listdir(IMAGE_PATH)
for path in dirs:
    if path not in images:
        os.remove(f"Images/{path}")

for url in images:
    im = Image.open(f"Images/{url}")
    cropped = im.crop((1642, 473, 3142, 1799))
    cropped.save(f"Images/new_{url}")
