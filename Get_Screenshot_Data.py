#import cv2
#import pytesseract
import re
import numpy as np

from google.cloud import vision
import datetime

"""
To run this you will need a driver:

In terminal run (Mac only):

brew install tesseract

May take a little while
"""


def extract_stats(image_path="screenshots/ss-2021-04-30 17:48:23.226436-1.jpg"):

    username = None
    kills = None
    deads = None
    T5_KillPoints = None
    T4_KillPoints = None
    text= None

    #img = cv2.imread(image_path, 0)
    #text = pytesseract.image_to_string(img)

    print(text)
    print('__________________________________________________________')

    KillPoints = re.findall('.*(Kill Points:.*[1-9])', text)

    #img = cv2.threshold(img, 10, 255, cv2.THRESH_TOZERO)[1]
    #text = pytesseract.image_to_string(img)

    print(text)
    print('__________________________________________________________')

    blur = cv2.GaussianBlur(img, (5, 5), 0)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #text = pytesseract.image_to_string(img)

    print(text)
    print('__________________________________________________________')

    Deads = re.findall('.*Dead (.*)', text)


    try:
        kills = KillPoints[0].split(': ')[1].replace('.', '').replace(',', '')
        deads = Deads[0].replace('.', '').replace(',', '')
    except:
        pass

    print('Kill Points: ', kills)
    print('Deaths: ', deads)

    #img = cv2.imread(image_path, 0)

    # print(img.shape)
    #img = img[265:300, 600:780]
    #img = cv2.threshold(img, 255, 255, cv2.THRESH_TRUNC
     #                   )[1]

    #text = pytesseract.image_to_string(img)

    print(text)
    print('__________________________________________________________')

    T4_KillPoints = text.replace('.', '').replace(',', '')

    # img = cv2.imread(image_path, 0)
    # img = img[290:320, 600:780]
    # img = cv2.threshold(img, 255, 255, cv2.THRESH_TRUNC
    #                     )[1]
    #
    # text = pytesseract.image_to_string(img)
    T5_KillPoints = text.replace('.', '').replace(',', '')

    print(text)
    print('__________________________________________________________')

    print('T4: ', T4_KillPoints)
    print('T5: ', T5_KillPoints)

    # THRESHOLDING FOR USERNAME

    # img = cv2.imread(image_path, 0)
    #
    # img = cv2.threshold(img, 170, 161, cv2.THRESH_TOZERO_INV)[1]
    #
    # text = pytesseract.image_to_string(img)

    print(text)
    print('__________________________________________________________')

    try:
        username = re.findall("""(.*):""", text)[0]
    except:
        print(text)

    print('User: ', username)

    return [{
        'username': str(username),
        'kill_points': str(kills),
        'dead': str(deads),
        't4_kill_points': str(T4_KillPoints),
        't5_kill_points': str(T5_KillPoints),
        'date': str(datetime.datetime.now())
    }]


def detect_text_uri(uri=""):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))