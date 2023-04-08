import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt
import time

path = 'images/'


def read_images(path):
    # Reading all the images in sequence
    for i in os.listdir(path):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = cv.imread(os.path.join(path, i))
            # cv.imshow('Original Images', img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()

        # if Q is pressed, the program skip to next image
        if 0xff == ord('q'):
            break

    return img


def oring_historgram():
    # histogram of o-rings
    for name in os.listdir(path):
        img = cv.imread(path + name)
        grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('images bud', grey)
        cv.waitKey(0)
        cv.destroyAllWindows()

        hist = cv.calcHist([img], [0], None, [256], [0, 256])
        plt.title('Histogram for gray scale picture')
        plt.xlabel('Gray Scale Value')
        plt.ylabel('# of Pixels')
        plt.plot(hist, color='gray')
        plt.xlim([0, 256])
        plt.show()


def getAverageGrey(img):
    # This returns average grey per pixel in an image
    sum = 0
    pixel = 0
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            sum += img[i, j]
            pixel += 1

            average_values = sum / pixel
            print(average_values)

    return average_values

def centerOfCircle(img):
    # This returns the center of a circle and places a red dot on it
    dimensions = img.shape
    width = dimensions[0]
    height = dimensions[1]
    halfWidth = width / 2
    halfHeight = height/ 2

    # Draw a red dot in the center of the image
    cv.circle(img, (int(halfWidth), int(halfHeight)), 2, (0, 0, 255), -1)
    cv.imshow('Center of Circle', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


    # Erosion
def erosion():
    for name in os.listdir(path):
        img = cv.imread(path + name)
        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv.erode(img, kernel, iterations=1)
        cv.imshow('Erosion', img_erosion)
        cv.waitKey(0)
        cv.destroyAllWindows()


def dilation():
    for name in os.listdir(path):
        img = cv.imread(path + name)
        kernel = np.ones((4, 4), np.uint8)
        img_dilation = cv.dilate(img, kernel, iterations=1)
        cv.imshow('Dilation', img_dilation)
        cv.waitKey(0)
        cv.destroyAllWindows()
