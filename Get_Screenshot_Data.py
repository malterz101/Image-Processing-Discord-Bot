
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


def detect_text_uri(uri="https://media.discordapp.net/attachments/880113505926262904/880855596792971324/Screenshot_20210827-173721_Rise_of_Kingdoms.png"):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    #

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    data = {}

    texts = "&&".join(str(texts).split('\\n'))

    try:
        pattern = re.compile("(?:.*?INFO)?&&(.*?)&&", re.MULTILINE|re.DOTALL)
        data['Name'] = re.findall(pattern, texts)[0].replace(',', '').replace('O ', '')
    except:
        data['Name'] = ''
    try:
        pattern = re.compile(".*?Power ?(.*?)&&", re.MULTILINE | re.DOTALL)
        data['Power'] = re.findall(pattern, texts)[0].replace(',', '').replace('.', '')
    except:
        data['Power'] = ''
    try:
        pattern = re.compile(".*?Kill Points ?(.*?)&&", re.MULTILINE | re.DOTALL)
        data['Kill Points'] = re.findall(pattern, texts)[0].replace(',', '').replace('.', '')
    except:
        data['Kill Points'] = ''
    try:
        pattern = re.compile("(?:.*?Dead)?&&(.*?)&&", re.MULTILINE | re.DOTALL)
        data['Deads'] = re.findall(pattern, texts)[0].replace(',', '').replace('.', '')
    except:
        data['Deads'] = ''

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    print('data')

    return data
