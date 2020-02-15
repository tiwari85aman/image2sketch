import cv2
import numpy as np


def image_algo_two(img):
    jc = cv2.imread(img)

    scale_percent = 1

    width = int(jc.shape[1] * scale_percent)
    height = int(jc.shape[0] * scale_percent)

    dim = (width, height)
    resized = cv2.resize(jc, dim, interpolation=cv2.INTER_AREA)

    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened = cv2.filter2D(resized, -1, kernel_sharpening)

    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    gauss = cv2.GaussianBlur(inv, ksize=(15, 15), sigmaX=0, sigmaY=0)

    def dodgeV2(image, mask):
        return cv2.divide(image, 255 - mask, scale=256)

    pencil_jc = dodgeV2(gray, gauss)

    return pencil_jc
