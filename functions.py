import cv2
import numpy as np
import os
import time
#  resize image 
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized

def mirror_image(image):
    return cv2.flip(image, 1)

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def change_light_conditin(image, state ):
    if state > 10':
        # return image
    # elif light_condit ion == 'night':
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
