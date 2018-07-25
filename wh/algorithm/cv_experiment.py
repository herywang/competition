# -*- coding: utf-8 -*-
'''
    python file describe: 利用opencv测试
'''
import cv2
import numpy as np


# filename = r"C:\Users\wangheng\Desktop\2018-6-23\f=25mm\5cm\8-2.bmp"

def morphological_transformation(image, distance, block_size):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # if distance == 3:
    #     block_size = 391
    # elif distance == 4:
    #     block_size = 341
    # else:
    #     block_size = 401

    thresh = cv2.adaptiveThreshold(image, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   thresholdType=cv2.THRESH_BINARY, blockSize=block_size, C=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    # cv2.imshow("dilate", dilate)
    return dilate


def get_contours(image, dilate_image, size = 100):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.erode(dilate_image, kernel, iterations=10)
    img, contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    con = get_max_contours(contours)
    x, y, w, h = cv2.boundingRect(con)
    # cv2.rectangle(img, (x, y), (x + w, y + h), 127, 3)
    # cv2.imshow("image", image[y+80:y+h-80, x+80:x+w-80])
    return dilate_image[y + size:y + h - size, x + size:x + w - size]


def get_max_contours(contours):
    max_con = 0
    _i = 0
    i = 0
    for c in contours:
        a = cv2.contourArea(c)
        if a > max_con:
            max_con = a
            _i = i
            i += 1
        else:
            i += 1
            continue
    return contours[_i]


def dilate_image(img, distance, size):
    # if distance == 3:
    #     size = 5
    # elif distance == 4:
    #     size = 9
    # else:
    #     size = 15
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
    dst = cv2.erode(img, kernel, iterations=2)
    return dst


"""
    直方图均衡化增加图像对比度
"""


def histogram_equalization(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))
    # cv2.namedWindow("res", 0)
    # cv2.imshow("res", res)
    return equ


"""
    Laplacian 算子局部对比度增加
"""


def laplacian_(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.array([[0, -1, 0],
                       [-1, 9, -1],
                       [0, -1, 1]])
    dst = cv2.filter2D(img, -1, kernel)
    return dst


def entrence(filename, distance=3, one=391, two=100, three=5):
    image = image = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = morphological_transformation(gray, distance, one)
    dst = get_contours(image, dst, size=two)
    # equ = laplacian_(dst)
    # cv2.imshow("equ", equ)
    dst = dilate_image(dst, distance, size=three)
    return dst
    # cv2.imshow("dst", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
