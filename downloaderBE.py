import os
import requests


def download(url: str, dest_folder: str):
    
    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    response = requests.get(url)
    if response.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Unable to download the file.")


download("https://docs.python.org/3/archives/python-3.10.2-docs-pdf-letter.zip", dest_folder="D:\Jagrati's Personal\Downloader")