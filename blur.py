"""The module allowing to transform an image into a blured one"""
import cv2
import os

def transblur(src, x, out):
    """
    Apllies a blur filter to an image
    :param src: The image to be blurred
    :param x: The strength of the blur
    :param out: The directory where the transformed images are stored
    """
    try:
        tmp = src[-4]
        for i in [-3, -2, -1]:
            tmp = tmp + src[i]
        if tmp == '.jpg' or tmp == '.png':
            image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
            if x < 0 or x % 2 == 0:
                print('Enter an odd and positive value')
                return
            else:
                blur = cv2.GaussianBlur(image,(x,x),0)
            # cv2.imshow("Blured Image", blur)
            cv2.imwrite(out, blur)
            return
        else:
            print(f'Not an image. EXTENSION={tmp} IN {src}')
    except cv2.error as e:
        print(f'ERROR={e}')