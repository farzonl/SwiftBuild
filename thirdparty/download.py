import urllib.request
import os.path
from pathlib import Path
import zipfile
import ssl

url1 = 'https://github.com/unicode-org/icu/releases/download/release-65-1/icu4c-65_1-Win64-MSVC2017.zip'
url2 = 'https://www.sqlite.org/2019/sqlite-amalgamation-3270200.zip'

def downloadAndExtract(url,name,outdir=''):
    filename = url[url.rfind("/")+1:]

    if not os.path.isfile(filename):
        print(f'Download {name}')
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(url, filename)

    dirname = Path(outdir + filename).with_suffix('')
    if not os.path.isdir(dirname):
        print(f'unzip {name}')
        with zipfile.ZipFile(filename,"r") as zip_ref:
            zip_ref.extractall(dirname)

downloadAndExtract(url1,'ICU')
downloadAndExtract(url2,'sqlite','../')
