import re
import csv
import requests
from bs4 import BeautifulSoup

base_url = "https://www.gitasupersite.iitk.ac.in"

def write_csv(filename,fields,rows):
    # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

def collect_details(chapter_num, shloka_num, soup_data, only_beng=False):

    shloka_div  = soup_data.find('div', class_='views-field-body')
    if not only_beng:
        hindi_div   = soup_data.find('div', class_='views-field-field-httyn')
        english_div = soup_data.find('div', class_='views-field-field-etpurohit')
        slkaudio    = soup_data.find(id='slkaudio')
        purohitAudio= soup_data.find(id='purohitAudio')
        tejAudio    = soup_data.find(id='tejAudio')

    data_list   =  [
        chapter_num,
        shloka_num,
        shloka_div.find_all('p')[0].text
    ]

    if not only_beng:
        data_list.append(hindi_div.find_all('p')[0].text)
        data_list.append(english_div.find_all('p')[0].text)
        data_list.append(base_url+slkaudio.find_all('source')[0].get("src")[1:])
        data_list.append(base_url+purohitAudio.find_all('source')[0].get("src")[1:])
        data_list.append(base_url+tejAudio.find_all('source')[0].get("src")[1:])

    sanitizesd_list = []
    for item in data_list:
        if type(item) == str:
            item = re.sub(r'\n+', '\n', item).strip()
        sanitizesd_list.append(item)

    return sanitizesd_list

if __name__ == '__main__':
    only_beng = True
    chapters = {
        "1": 47,
        "2": 72,
        "3": 43,
        "4": 42,
        "5": 29,
        "6": 47,
        "7": 30,
        "8": 28,
        "9": 34,
        "10": 42,
        "11": 55,
        "12": 20,
        "13": 35,
        "14": 27,
        "15": 20,
        "16": 24,
        "17": 28,
        "18": 78
    }

    if only_beng:
        csv_headers = ['chapter_num', 'shloka_num', 'shloka']
    else:
        csv_headers = ['chapter_num', 'shloka_num', 'shloka', 'hindi', 'english', 'slkaudio', 'purohitAudio', 'tejAudio']

    for chapter, shlokas in chapters.items():
        # print(f"Key : {chapter} and value : {shlokas}\n")
        main_dict = list()
        for number in range(1,shlokas+1):
            print(f"Chapter {chapter}: Verse {number}")
            if only_beng:
                url = f"{base_url}/srimad?language=bn&field_chapter_value={chapter}&field_nsutra_value={number}"
            else:
                url = f"{base_url}/srimad?show_mool=1&show_purohit=1&show_tej=1&httyn=1&etpurohit=1&&language=dv&field_chapter_value={chapter}&field_nsutra_value={number}"
            req       = requests.get(url)
            soup      = BeautifulSoup(req.content,'html.parser')
            dict_data = collect_details(chapter, number, soup, only_beng)
            main_dict.append(dict_data)

        write_csv(f"Chapter-{chapter}.csv",csv_headers,main_dict)

    print("Completed execution")