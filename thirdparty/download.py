import wget
import os.path
import zipfile

url = 'https://github.com/unicode-org/icu/releases/download/release-65-1/icu4c-65_1-Win64-MSVC2017.zip'
filename = url[url.rfind("/")+1:]

if not os.path.isfile(filename):
    print('Download ICU')
    wget.download(url, filename)

dirname = os.path.splitext(filename[0])
if not os.path.isdir(dirname):
    print('unzip ICU')
    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(dirname)
