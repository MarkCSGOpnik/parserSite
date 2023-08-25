import re
import math
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import openpyxl
from openpyxl.workbook import Workbook
import requests
import os
import chardet

parsing_list = openpyxl.load_workbook('parsing.xlsx')
sheet = parsing_list.active
parsing = parsing_list['list1']

folder_path = "all.htm"

num_all = 2

path = "C:\\\\Users\\\\user\\\\PycharmProjects\\\\pythonProject\\\\all.htm\\\\"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    new_file_path = file_path.replace("all.htm\\", "")
    all_path = path + new_file_path
    print(all_path)

    with open(all_path, 'r', encoding='cp1251', errors='ignore') as primaryFile:
        soup = BeautifulSoup(primaryFile, "lxml")

    page = soup.find_all("td")

    page_str = str(page)

    with open("td.htm", "w") as tdFile:
        tdFile.write(page_str)

    with open("td.htm",  'r', encoding='cp1251', errors='ignore') as tdFile:
        soup = BeautifulSoup(tdFile, "lxml")

    pc_user_name = soup.find(string="Компьютер  ").find_next().text

    parsing['C' + str(num_all)] = pc_user_name

    parsing.save('parsing.xlsx')

    computer_type = soup.find(string="Тип компьютера  ").find_next().text

    substring_mobile = "Mobile"

    if substring_mobile in computer_type:
        pc_or_mobile = "Ноутбук"
    else:
        pc_or_mobile = "Компьютер"

    pc_or_mobile_in = "G" + str(num_all)
    parsing[pc_or_mobile_in] = pc_or_mobile
    cpu = soup.find(string="Тип ЦП  ").find_next().text

    parsing['H' + str(num_all)] = cpu

    parsing.save('parsing.xlsx')

    storagePc = soup.find_all(string="Размер  ")

    sum_ram = 0

    for item in storagePc:
        if "ГБ" in item.find_next().text:
            sizeCpu = item.find_next().text.replace("ГБ", "")
            sum_ram += int(sizeCpu)

    ram = str(sum_ram)
    ram += " ГБ"

    type_ram_element = soup.find(string="Форм-фактор  ")
    if type_ram_element:
        type_ram = type_ram_element.find_next().find_next().find_next().find_next().find_next().find_next().text
    else:
        type_ram = ""

    parsing['I' + str(num_all)] = ram + " " + type_ram

    parsing.save('parsing.xlsx')

    search_motherboard = soup.find_all(string="Версия  ")
    range_num = 0
    for item in search_motherboard:
        range_num += 1
        if range_num == 3:
            motherboard = str(item.find_next().text)
            parsing["J" + str(num_all)] = motherboard

    range_num = 0

    disk_all = soup.find_all(string="Дисковый накопитель  ")

    for item in disk_all:
        if "ГБ" in item.find_next().text:
            if "SSD" in item.find_next().text:
                ssd_disk = item.find_next().text
                parsing["K" + str(num_all)] = ssd_disk
            else:
                if not "USB" in item.find_next().text:
                    disk = item.find_next().text
                    parsing["K" + str(num_all)] = disk

    video_card = soup.find(string="Видеоадаптер  ").find_next().text

    parsing['M' + str(num_all)] = video_card

    parsing.save('parsing.xlsx')

    operation = soup.find_all(string="Операционная система  ")
    for item in operation:
        range_num += 1
        if range_num == 2:
            operation_system = item.find_next().text
            parsing['N' + str(num_all)] = operation_system
    if "64" in soup.find(string="Тестовый модуль  ").find_next().text:
        bit = str("64")
    else:
        bit = str("32")
    parsing["O" + str(num_all)] = bit

    parsing.save('parsing.xlsx')

    num_all += 1



