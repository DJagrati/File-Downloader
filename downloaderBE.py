import os
import requests
from requests.exceptions import MissingSchema

filename = "" 
def isDownloadable(url: str):
    global response, filename
    response = getResponse(url)
    if not(response == None):
        if response.ok:   #For 2xx status code
            filename = url.split('/')[-1].replace(" ", "_")  
            return True
        else:   #For non-2xx status codes (4xx or 5xx)
            return False
    else: 
        return False

#An handled method to get the response based on different type of URLs provided.
def getResponse(url):
    try:
        return requests.get(url)
    except MissingSchema:
        return None


def downloadFile(dest_folder: str):
    file_path = os.path.join(dest_folder, filename)  #Path where file will download.
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 8):  #Iterating on response in chunks and writing it in the filepath(in short downloading it)
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
