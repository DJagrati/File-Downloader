import os
import requests
from requests.exceptions import MissingSchema
from threading import Thread

filename = ""  # be careful with file names
def isDownloadable(url: str):
    global response, filename
    response = getResponse(url)
    if not(response == None):
        if response.ok:
            filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
            return True
        else:  # HTTP status code 4XX/5XX
            return False
    else: 
        return False

def getResponse(url):
    try:
        return requests.get(url)
    except MissingSchema:
        return None


def downloadFile(dest_folder: str):
    file_path = os.path.join(dest_folder, filename)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())

def startDownload(destFolder):
    Thread(target=downloadFile(destFolder)).start
    

# download("https://docs.python.org/3/archives/python-3.10.2-docs-pdf-letter.zip", dest_folder="D:\Jagrati's Personal\Downloader")