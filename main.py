import re
import math
from bs4 import BeautifulSoup
import requests
import os


with open("admin2.htm",  'r', encoding='cp1251', errors='ignore') as primaryFile:
    soup = BeautifulSoup(primaryFile, "lxml")

page = soup.find_all("td")

page_str = str(page)

with open("td.htm", "w") as tdFile:
    tdFile.write(page_str)

with open("td.htm",  'r', encoding='cp1251', errors='ignore') as tdFile:
    soup = BeautifulSoup(tdFile, "lxml")

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

sumRam = 0

for item in storagePc:
    if "ГБ" in item.find_next().text:
        sizeCpu = item.find_next().text.replace("ГБ","")
        sumRam += int(sizeCpu)

ram = str(sumRam)
ram += " ГБ"
print(ram)

TypeRam = soup.find(string="Тип памяти  ").find_next().text
print(TypeRam)

searchMotherboard = soup.find_all(string="Версия  ")
rangeNum = 0
for item in searchMotherboard:
    rangeNum += 1
    if rangeNum == 3:
        motherBoard = str(item.find_next().text)
        print(motherBoard)

rangeNum=0

diskAll = soup.find_all(string="Дисковый накопитель  ")

for item in diskAll:
    if "ГБ" in item.find_next().text:
        if "SSD" in item.find_next().text:
            print(item.find_next().text)
            ssdDisk = item.find_next().text
        else:
            if not "USB" in item.find_next().text:
                print(item.find_next().text)
                disk = item.find_next().text

videoCard = soup.find(string="Видеоадаптер  ").find_next().text
print(videoCard)

operation = soup.find_all(string="Операционная система  ")
for item in operation:
    rangeNum += 1
    if rangeNum == 2:
        operationSystem = item.find_next().text
        print(operationSystem)




