# IMPORTS -----------------
import os
import re
import json
import requests
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# -------------------------

def loadJsonFile(json_file_path):
    """Loads JSON file from the given path.

    Tries to open the file, read its content and parse it as a JSON.

    Args:
        json_file_path (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing 'status', 'message' and 'data' keys.
        'data' key contains the JSON data.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        JSONDecodeError: If the JSON file cannot be decoded.
        Exception: If an unexpected error occurs.

    """

    try:
        with open(json_file_path, 'r') as f:
            image_urls = json.load(f)

        return {
            'status' : True,
            'message': 'success',
            'data'   : image_urls
        }  # Return the image_urls

    except FileNotFoundError as e:
        return {
            'status' : False,
            'message': f"Error: JSON file '{json_file_path}' not found: {e}",
            'data'   : {}
        }  # Return the error

    except json.JSONDecodeError as e:
        return {
            'status' : False,
            'message': f"Error: Failed to decode JSON file '{json_file_path}': {e}",
            'data'   : {}
        }  # Return the error

    except Exception as e:
        return {
            'status' : False,
            'message': f"An unexpected error occurred: {e}",
            'data'   : {}
        }  # Return the error

def downloadImages(image_files, download_folder):
    """
    Downloads images from a list of URLs and stores them in a specified folder.

    Parameters:
        image_files (list): A list of URLs pointing to the images to be downloaded.
        download_folder (str): The path to the folder where the images will be stored.

    Returns:
        None

    This function first creates the specified download folder if it doesn't exist,
    using the 'exist_ok' parameter of the 'makedirs' function to avoid raising an
    exception if the directory already exists.

    Then it iterates over the list of image URLs and attempts to download each image.
    """
    # Create the directory if not present
    os.makedirs(download_folder,exist_ok=True)


    # Download the images and store in the folder
    print(f"\nDownloading Files\n-------------------\n")
    for i,url in enumerate(image_files, start=1):
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(download_folder,f"image_{i}.jpg")
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {url} => {filename}")
        else:
            print(f"Failed to download {url} => {response.status_code}")

    print(f"\n-------------------\nDownloading Files Completed\n")

def natural_sort_key(s):
    """
    Takes a string as input and returns a list of its characters, with any
    consecutive digits (as identified by the regular expression '\d+') replaced
    by their integer value.

    For example, the input string "a1b2c3" would be split into the list
    ['a', 1, 'b', 2, 'c', 3].

    This function is used to provide a natural sort order for a list of strings
    that may contain numbers embedded in them. Without this function, the
    sorted() function would sort the list in alphabetical order, which in this
    case would be ['a', 'b', 'c', 1, 2, 3]. Instead, this function returns a list
    that can be sorted in the desired order: ['a', 1, 'b', 2, 'c', 3].

    The regular expression '\d+' matches one or more digits in a row. The 're.split'
    function splits the input string using this regular expression as the delimiter,
    which results in a list of substrings. The list comprehension then iterates
    over this list, checking each substring to see if it is a digit or not. If it
    is a digit, the integer value of the digit is returned in its place. If it is
    not a digit, the original substring is returned unchanged. The resulting
    list is then returned as the output of the function.
    """
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', s)]


def generatePdfFromImages(output_pdf_file, download_folder):
    """
    Generates a PDF file from a list of images in a folder.

    The function assumes that the images are in JPEG format and sorts them using
    a natural sort order.

    The function creates a Reportlab canvas object with the A4 page size and
    generates a PDF page for each image in the sorted image list.

    Args:
        output_pdf_file (str): The filename for the generated PDF
        download_folder (str): The folder containing the images to include in
            the PDF

    Returns:
        None
    """
    print(f"\PDF Generation Started\n-------------------\n")

    c = canvas.Canvas(output_pdf_file, pagesize=A4)

    image_files = sorted(os.listdir(download_folder), key=natural_sort_key)
    for image_file in image_files:
        if image_file.lower().endswith('.jpg') or image_file.lower().endswith('.jpeg'):
            image_path = os.path.join(download_folder, image_file)
            c.drawImage(image_path, 0, 0, width=A4[0], height=A4[1])
            c.showPage()
    c.save()

    print(f"\n-------------------\nPDF Generated {output_pdf_file}\n")



def generateImageToPDF(json_file_path, download_folder, output_pdf_file):
    """
    Generates a PDF file from a JSON file containing a list of URLs to images.

    The function first loads the JSON file and attempts to download the images
    from the URLs. If the download is successful, it generates a PDF file from
    the downloaded images.

    If the JSON file cannot be loaded or if the download fails, the function
    will print an error message and exit without generating a PDF file.

    Args:
        json_file_path (str): The path to the JSON file containing the URLs to
            images.
        download_folder (str): The path to the folder where the images will be
            downloaded.
        output_pdf_file (str): The path to the PDF file to be generated.

    Returns:
        None
    """

    load_image_files = loadJsonFile(json_file_path)
    if load_image_files['status']:
        downloadImages(load_image_files['data'], download_folder)
        generatePdfFromImages(output_pdf_file,download_folder)
    else:
        print(load_image_files['message'])



if __name__ == "__main__":
    generateImageToPDF('image_urls.json', 'downloaded_images', 'output.pdf')