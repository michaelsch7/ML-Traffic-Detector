import pandas as pd
from sodapy import Socrata
import requests
import time


def printCityplace():
  pics = 2275
  while True and pics < 2750:
    url = "https://511la.org/map/Cctv/b25--1"
    response = requests.get(url)

    with open(f"i10-cityplace/{pics}_img_I10_Cityplace.jpg", "wb") as file:
        file.write(response.content)
    pics = pics+1
    time.sleep(11)
