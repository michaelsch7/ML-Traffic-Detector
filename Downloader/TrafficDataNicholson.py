import pandas as pd
from sodapy import Socrata
import requests
import time


def printNicholson():
  pics = 1600
  while True and pics < 2100:
    url = "https://511la.org/map/Cctv/b19--1"
    response = requests.get(url)

    with open(f"i10-nicholson/{pics}_img_I10_Nicholson.jpg", "wb") as file:
        file.write(response.content)
    pics = pics+1
    time.sleep(11)
