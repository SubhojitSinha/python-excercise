import requests
import traceback

def write_to_file(file_name, text):
    with open(file_name, "w") as file:
        file.write(str(text))

def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes}:{seconds}"

def generate_youtube_string_from_url_bs4(input_url):
    from bs4 import BeautifulSoup
    """
    Collects the input from the user, validates the URL, and retrieves the title,
    thumbnail, and description of the YouTube video based on the provided URL.
    """
    # validate if the url is available and workin
    response = requests.get(input_url)

    if response.status_code == 200:
        soup        = BeautifulSoup(response.content, "html.parser")
        title       = soup.find("meta", property="og:title")["content"]
        thumbnail   = soup.find("meta", property="og:image")["content"]
        description = soup.find("meta", property="og:description")["content"]

        # print the output
        if thumbnail:
            return {
                "status" : True,
                "message": "success",
                "data": {
                    "title"      : title,
                    "author"     : "",
                    "input_url"  : input_url,
                    "thumbnail"  : thumbnail,
                    "description": description,
                    "duration"   : ""
                }
            }
        else:
            raise Exception("Thumbnail not found, please try again")
    else:
        raise Exception("URL is not valid, please try again")

def generate_youtube_string_from_url_ytdl(input_url):
    import youtube_dl
    """
    Collects the input from the user, validates the URL, and retrieves the title,
    thumbnail, and description of the YouTube video based on the provided URL.
    """

    # validate if the url is available and workin
    response = requests.get(input_url)
    if response.status_code == 200:
        video_info  = youtube_dl.YoutubeDL({'quiet': True}).extract_info(url = input_url,download=False)
        title       = video_info.get('title')
        author      = video_info.get('uploader')
        thumbnail   = video_info.get('thumbnail')
        duration    = video_info.get('duration')
        description = video_info.get('description')[:150]+"..."
        if thumbnail:
            return {
                "status" : True,
                "message": "success",
                "data": {
                    "title"      : title,
                    "author"     : author,
                    "input_url"  : input_url,
                    "thumbnail"  : thumbnail,
                    "description": description,
                    "duration"   : duration
                }
            }
        else:
            raise Exception("Thumbnail not found, please try again")
    else:
        raise Exception("URL is not valid, please try again")

def sort_list_by_duration(data):
    """
    Sorts a list by duration using the 'duration' key as the sorting key.

    Args:
        data (list): The input list to be sorted.

    Returns:
        list: The sorted list.
    """
    return sorted(data, key=lambda x: x['duration'])


if __name__ == "__main__":
    try:
        # Getting the inputs
        input_ids   = input("\n\nA. Enter YouTube token[s]: ")
        input_type  = input("\nB.Select Method:\n-- 1. BeautifulSoup\n-- 2. Youtube-dl\n-- Enter your choice? [1/2] : ")

        # Identifying the method
        method_name = 'generate_youtube_string_from_url_ytdl' if input_type == "2" else 'generate_youtube_string_from_url_bs4'

        # Creating the list of full urls
        base_url = "https://www.youtube.com/watch?v="
        urls = [base_url+x for x in input_ids.split(',')]

        #   Collecting the list of data
        data_set = []
        for url in urls:
            data = eval(method_name+f"('{url}')")
            if(data['status']):
                data_set.append(data['data'])

        if input_type == "2":
            data_set = sort_list_by_duration(data_set)

        if data_set:
            formatted_text = ''
            if input_type == "2":
                for data in data_set:
                    formatted_text = f"\n\n### {data['title']} - by {data['author']} - [ {convert_seconds_to_hms(data['duration'])} ]\n {data['description']}\n\n[<img src='{data['thumbnail']}' width='350' alt='{data['title']}' />]({data['input_url']} '{data['title']}')"
                    print(formatted_text)
            else:
                for data in data_set:
                    formatted_text = f"\n\n### {data['title']}\n {data['description']}\n\n[<img src='{data['thumbnail']}' width='350' alt='{data['title']}' />]({data['input_url']} '{data['title']}')"
                    print(formatted_text)

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        exit()