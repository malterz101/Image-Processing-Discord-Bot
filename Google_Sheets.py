# Required for Google Sheets API
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import pandas as pd
import gspread
import gspread_dataframe as gd

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]


CONFIGURATION_SHEET = "1_5_jLemOoBH4rYrAEo0xjIDZ22q00bveIGM0GYKMvac" # https://docs.google.com/spreadsheets/d/1_5_jLemOoBH4rYrAEo0xjIDZ22q00bveIGM0GYKMvac/edit?usp=sharing

def Connect_To_Google_Sheets(values=
            [{
                'datetime': '1000',
                'player': 'MADBilbo',
                'killpoints': '283,785,668',
                't4': '211607230',
                't5': '58486660',
                'dead': '2,229,181',
                't4Kills': None,
                't5Kills': None,
                'farmer': None,
                'kd': '2129'
            }]
        ):

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    body = pd.DataFrame(
        data=values
    )

    gc = gspread.service_account("credentials.json")
    sheet = gc.open_by_key(CONFIGURATION_SHEET).worksheet("BagginsBot")
    # sheet.add_rows(body.shape[0])
    existing = gd.get_as_dataframe(sheet)
    updated = existing.append(body)
    gd.set_with_dataframe(
        sheet,
        updated,
        include_index=False,
        include_column_header=True,
        resize=True
    )



    return values

