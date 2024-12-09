import pandas as pd
from sodapy import Socrata
import requests
import time


def printAcadianDrive():
  pics = 2500
  while True and pics < 3000:
    url = "https://511la.org/map/Cctv/b23.C1--1"
    response = requests.get(url)

    with open(f"i10-acadian/{pics}_img_I10_Acadian.jpg", "wb") as file:
        file.write(response.content)
    pics = pics+1
    time.sleep(11)
