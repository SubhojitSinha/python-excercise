import os
import re
import csv
import requests
from bs4 import BeautifulSoup
from const import colours

base_url = "https://sarat-rachanabali.nltr.org/"
start_page = ""
file_name = ""
story_name = ""

def fetch_page_content(page_ref):
    req           = requests.get(page_ref)
    soup          = BeautifulSoup(req.content, 'html.parser')

    for br in soup.find_all("br"):
        br.replace_with("\n")

    page_content  = soup.find(id='mainContent').text.strip()
    hddnCatId     = soup.find('input', {'name' : 'hddnCatId'     })['value']
    hddnLekhaId   = soup.find('input', {'name' : 'hddnLekhaId'   })['value']
    hddnParchadId = soup.find('input', {'name' : 'hddnParchadId' })['value']
    hddnPageNo    = soup.find('input', {'name' : 'hddnPageNo'    })['value']
    totalPage     = soup.find('input', {'name' : 'hddnPage'      })['value']


    return {
        'total_pages': totalPage,
        'content'    : page_content,
        'next_url'   : f"{base_url}nextPageGen.jsp?{hddnCatId}{hddnLekhaId}{hddnParchadId}{hddnPageNo}"
    };

def generate_file_from_url(page_url,story_name,page_progress= False):
    first_run = fetch_page_content(page_url)
    content   = first_run['content']
    totalPage = int(first_run['total_pages'])
    next_url  = first_run['next_url']

    for x in range(1, totalPage):

        data     = fetch_page_content(next_url)
        next_url = data['next_url']
        content  = content + '\n\n' +data['content']

        if page_progress:
            print (f"Novel = {story_name} {colours.OKGREEN} Page {x} of {totalPage}{colours.ENDC} | {colours.FAIL}{int((x/totalPage)*100)}%{colours.ENDC}",end='\r', flush=True)


    if page_progress:
        print (f"Novel = {story_name} {colours.OKGREEN} Page {totalPage} of {totalPage}{colours.ENDC} | {colours.FAIL}100%{colours.ENDC}",end='', flush=True)

    f = open(f'{story_name}.txt', 'w')
    f.write(content)
    f.close()

def get_all_stories(url):
    req  = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    all_href = soup.find_all('a', href=re.compile('content\.jsp'))
    count = 0
    for x in all_href:
        count+=1

        story_name = x.text.strip()
        story_url  = f"{base_url}{x['href']}"
        print(f"{count}. {story_name} = {story_url}", end='',flush=True)
        generate_file_from_url(story_url,story_name)
        print (f"| {colours.OKGREEN}DONE{colours.ENDC} | {colours.FAIL}{int(count/len(all_href)*100)}%{colours.ENDC} complete", flush=True)


def get_valid_type_input(prompt):
    while True:
        type = input(prompt)
        try:
            if type.lower() == 's' or type.lower() == 'n':
                return type.lower()
            else:
                print(f"{colours.FAIL}Please enter 's' for stories and 'n' for novel.{colours.ENDC}")
        except ValueError:
            print(f"{colours.FAIL}Please enter 's' for stories and 'n' for novel.{colours.ENDC}")

# The main funtion
if __name__ == '__main__':
    os.system('clear')
    source_url =  input("Source URL:  ")
    story_name =  input("Story Name:  ")
    stories_or_novel = get_valid_type_input("Stories Or Novel? [s/n]: ")

    print("\n----------------------------\n\n")
    print(f"Trying to collect {colours.OKBLUE}`{story_name}`{colours.ENDC} for you. Please wait...\n")
    print("\n----------------------------\n\n")

    if stories_or_novel == 's':
        get_all_stories(source_url)
    elif stories_or_novel == 'n':
        generate_file_from_url(source_url, story_name, page_progress= True)
    else:
        print(f"{colours.FAIL}INVALID.{colours.ENDC}")

    print(f"{colours.OKGREEN}Completed execution{colours.ENDC}")
