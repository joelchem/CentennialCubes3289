import cv2 as cv
import numpy as np
import json


image_list = [
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
for i in range(len(image_list)):
    image_list[i] = f"new_{image_list[i]}"

prev_img = None
prev_yuv = None
for i in range(len(image_list)):
    img_path = f"Images/{image_list[i]}"
    img = cv.imread(img_path)
    yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    if i > 0:
        avg = np.mean(yuv[:,:,0])
        prev_avg = np.mean(prev_yuv[:,:,0])
        delta = avg - prev_avg
        print(f"Change in average luminosity of {delta}")
    prev_img = img
    prev_yuv = yuv
