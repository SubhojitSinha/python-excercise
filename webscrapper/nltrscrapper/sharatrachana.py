import re
import csv
import requests
from bs4 import BeautifulSoup
from const import colours

base_url = "https://sarat-rachanabali.nltr.org/"

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

def generate_file_from_url(page_url,story_name):
    first_run = fetch_page_content(page_url)
    content   = first_run['content']
    totalPage = first_run['total_pages']
    next_url  = first_run['next_url']

    for x in range(1, int(totalPage)):
        data     = fetch_page_content(next_url)
        next_url = data['next_url']
        content  = content + '\n\n' +data['content']

    f = open(f'{story_name}.txt', 'w')
    f.write(content)
    f.close()

# The main funtion
if __name__ == '__main__':
    req  = requests.get(f'{base_url}subCat.jsp?002')
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

    print("Completed execution")
