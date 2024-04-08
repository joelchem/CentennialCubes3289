import cv2 as cv
import numpy as np
import json

with open("image_list.json") as f:
    image_list = json.load(f)

THRESHOLD = -20

prev_img = None
prev_yuv = None
for i in range(len(image_list)):
    img_path = image_list[i]
    img = cv.imread(img_path)
    yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    if i > 0:
        assert prev_yuv != None
        avg = np.mean(yuv[:,:,0])
        prev_avg = np.mean(prev_yuv[:,:,0])
        delta = avg - prev_avg
        print(f"Change in average luminosity of {delta}")
        if avg - prev_avg < THRESHOLD:
            print(f"Power outage detected, delta is less than {THRESHOLD}")
    prev_img = img
    prev_yuv = yuv
