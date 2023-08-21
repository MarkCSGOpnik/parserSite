import re
import math
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

pcUserName = soup.find(string="Компьютер  ").find_next().text

print(pcUserName)

computerType = soup.find(string=("Тип компьютера  ")).find_next().text

substringMobile = "Mobile"

if substringMobile in computerType:
    pcOrMobile = "Ноутбук"
else:
    pcOrMobile = "Компьютер"

print(pcOrMobile)

cpu = soup.find(string="Тип ЦП  ").find_next().text
print(cpu)

storagePc = soup.find_all(string="Размер  ")

for item in storagePc:
    unit = item.find_next().text.replace(item.split()[0], "")
    print(unit)
    if unit != "МБ":
        print(item.find_next().text)

