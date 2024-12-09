import pandas as pd
from sodapy import Socrata
import requests
import time


def printCollegeDrive():
  pics = 2275
  while True and pics < 3:
    url = "https://511la.org/map/Cctv/b24--1"
    response = requests.get(url)

    with open(f"s3a://bucket-michaels/dev/input/i10-college/{pics}_img_I10_collegeDr.jpg", "wb") as file:
        file.write(response.content)
    pics = pics+1
    time.sleep(11)
