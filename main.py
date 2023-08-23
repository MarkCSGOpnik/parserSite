import re
import math
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import requests
import os


with open("C:\\Users\\user\\PycharmProjects\\pythonProject\\all.htm\\1904-adm.htm", 'r', encoding='cp1251', errors='ignore') as primaryFile:
    soup = BeautifulSoup(primaryFile, "lxml")

page = soup.find_all("td")

page_str = str(page)

with open("td.htm", "w") as tdFile:
    tdFile.write(page_str)

with open("td.htm",  'r', encoding='cp1251', errors='ignore') as tdFile:
    soup = BeautifulSoup(tdFile, "lxml")

pc_user_name = soup.find(string="Компьютер  ").find_next().text

print(pc_user_name)

computer_type = soup.find(string="Тип компьютера  ").find_next().text

substring_mobile = "Mobile"

if substring_mobile in computer_type:
    pc_or_mobile = "Ноутбук"
else:
    pc_or_mobile = "Компьютер"

print(pc_or_mobile)

cpu = soup.find(string="Тип ЦП  ").find_next().text
print(cpu)

storagePc = soup.find_all(string="Размер  ")

sum_ram = 0

for item in storagePc:
    if "ГБ" in item.find_next().text:
        sizeCpu = item.find_next().text.replace("ГБ", "")
        sum_ram += int(sizeCpu)

ram = str(sum_ram)
ram += " ГБ"
print(ram)

type_ram_element = soup.find(string="Форм-фактор  ")
if type_ram_element:
    type_ram = type_ram_element.find_next().find_next().find_next().find_next().find_next().find_next().text
else:
    type_ram = "нет"
print(type_ram)

search_motherboard = soup.find_all(string="Версия  ")
range_num = 0
for item in search_motherboard:
    range_num += 1
    if range_num == 3:
        motherboard = str(item.find_next().text)
        print(motherboard)

range_num = 0

disk_all = soup.find_all(string="Дисковый накопитель  ")

for item in disk_all:
    if "ГБ" in item.find_next().text:
        if "SSD" in item.find_next().text:
            print(item.find_next().text)
            ssd_disk = item.find_next().text
        else:
            if not "USB" in item.find_next().text:
                print(item.find_next().text)
                disk = item.find_next().text

video_card = soup.find(string="Видеоадаптер  ").find_next().text
print(video_card)

operation = soup.find_all(string="Операционная система  ")
for item in operation:
    range_num += 1
    if range_num == 2:
        operation_system = item.find_next().text
        print(operation_system)
if "64" in soup.find(string="Тестовый модуль  ").find_next().text:
    bit = "64"
else:
    bit = "32"
print(bit)



