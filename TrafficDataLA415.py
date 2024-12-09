import pandas as pd
from sodapy import Socrata
import requests
import time


def printLA415():
  pics = 1500
  while True and pics < 2000:
    url = "https://511la.org/map/Cctv/b17--1"
    response = requests.get(url)

    with open(f"i10-la415/{pics}_img_I10_LA415.jpg", "wb") as file:
        file.write(response.content)
    pics = pics+1
    time.sleep(11)