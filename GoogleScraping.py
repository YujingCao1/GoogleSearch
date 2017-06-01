# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:05:38 2017

@author: caoyujin
"""
import requests
from bs4 import BeautifulSoup

url = raw_input("Enter a website to extract the URL's from: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)