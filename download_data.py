import os
import urllib.request
import zipfile
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup

PATH_TO_STORE_CSVS = "./data"
DOWNLOAD_BASE_URL = "http://data.gdeltproject.org/events/"


def extract_from_url(url: str) -> None:
    # open url
    resp = urlopen(DOWNLOAD_BASE_URL + url)
    # read zipfile
    zipfile = ZipFile(BytesIO(resp.read()))
    # get the csv file name
    fname = zipfile.namelist()[0]
    # extract to data
    zipfile.extractall(PATH_TO_STORE_CSVS)
    # close zipfile we don't need
    zipfile.close()
    
    # let me know how much it is completed.
    print(f'{fname} Completed')


def main():
    all_files_url = "http://data.gdeltproject.org/events/index.html"
    all_files = requests.get(all_files_url)
    soup = BeautifulSoup(all_files.content)

    for a in soup.find_all("a"):
        url = a["href"]
        if "export" not in url:
            continue
        extract_from_url(url)


if __name__ == "__main__":
    main()