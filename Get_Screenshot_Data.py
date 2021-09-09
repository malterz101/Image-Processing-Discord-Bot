
import re
import numpy as np
import os

from google.cloud import vision
import datetime
import json


def detect_text_uri(uri="https://media.discordapp.net/attachments/880113505926262904/880855596792971324/Screenshot_20210827-173721_Rise_of_Kingdoms.png"):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    with open("credentials.json", "w+") as f:
        credentials = json.dump(json.loads(os.environ.get("GOOGLE_CREDENTIALS", None)), f)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    data = {}

    texts = "&&".join(str(texts).split('\\n')).replace('.', '').replace(',', '')

    if not texts.__contains__('/'):
        try:
            pattern = re.compile("&&O (.*?)&&", re.MULTILINE | re.DOTALL)
            data['Name'] = re.findall(pattern, texts)[0].replace(',', '').replace('O ', '')
        except:
            data['Name'] = ''

        pattern = re.compile('(?:&&O .*?&&).*&&')
        texts = re.findall(pattern, texts)

        pattern = re.compile('.*?([0-9]*)')
        try:
            results = list(filter(None, re.findall(pattern, texts[0])))
        except:
            results = texts

        try:
            data['Power'] = results[0]
        except:
            data['Power'] = ''

        try:
            data['Kill Points'] = results[1]
        except:
            data['Kill Points'] = ''

        try:
            data['Dead'] = results[17]
        except:
            data['Dead'] = results
    else:
        try:
            pattern = re.compile(".*([a-zA-Z0-9]*)", re.MULTILINE|re.DOTALL)
            data['Name'] = re.findall(pattern, texts)[1].replace(',', '').replace('', '')
        except:
            data['Name'] = ''

        pattern = re.compile('(?:&&O .*?&&).*&&')
        texts = re.findall(pattern, texts)

        pattern = re.compile('.*?([0-9]*)')
        try:
            results = list(filter(None, re.findall(pattern, texts[0])))
        except:
            results = [texts]

        try:
            data['Power'] = results[0]
        except:
            data['Power'] = ''

        try:
            data['Kill Points'] = results[1]
        except:
            data['Kill Points'] = ''

        try:
            data['Dead'] = results[5]
        except:
            data['Dead'] = ''


    print(data)


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return data
