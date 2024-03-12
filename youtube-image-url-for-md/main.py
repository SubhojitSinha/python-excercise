import requests
from bs4 import BeautifulSoup

def write_to_file(file_name, text):
    with open(file_name, 'a') as f:
        f.write(str(text))
        print("written to file")

def generate_youtube_string_from_url():
    # Collect the input from user
    input_url = input("Enter YouTube URL: ")

    # validate if the url is available and workin
    response = requests.get(input_url)

    if response.status_code == 200:
        # parse the html content using bs4
        soup = BeautifulSoup(response.content, "html.parser")

        # find the thumbnail title
        title = soup.find("meta", property="og:title")["content"]

        # find the thumbnail image
        thumbnail = soup.find("meta", property="og:image")["content"]

        # find the video description
        description = soup.find("meta", property="og:description")["content"]

        # print the output
        if thumbnail:
            return_text = f"\n\n### {title}\n {description}\n[![{title}]({thumbnail})]({input_url} '{title}')"

            print(return_text)
            exit()
        else:
            print("Thumbnail not found, please try again")
            exit()
    else:
        print("URL is not valid, please try again")
        exit()

if __name__ == "__main__":
    generate_youtube_string_from_url()