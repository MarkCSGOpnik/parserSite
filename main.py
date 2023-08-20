import re

from bs4 import BeautifulSoup
import requests
import os


with open("admin2.htm",  'r', encoding='cp1251', errors='ignore') as file:
    soup = BeautifulSoup(file, "lxml")

page = soup.find_all("td")

page_str = str(page)

with open("td.htm", "w") as file:
    file.write(page_str)

with open("td.htm",  'r', encoding='cp1251', errors='ignore') as file:
    soup = BeautifulSoup(file, "lxml")

pc_user_name_element = soup.find(string="Компьютер  ").find_next().text

print(pc_user_name_element)
##gkf
##dfudfuh