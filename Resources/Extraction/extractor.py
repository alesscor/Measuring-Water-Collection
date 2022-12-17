import sys
import os
from bs4 import BeautifulSoup
import requests
sys.path.append("/.../Extraction")
import herramientas_extraccion as he

def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for year in range(2020,2023,1):
    DIRECTORIO_I = he.DIRECTORIO_RAIZ + "\\Datos\\CMORPH"
    os.makedirs(DIRECTORIO_I, exist_ok=True)
    for month in range(1,13,1):
        if year==he.URL_ULTIMO_AÑO_MES[0] and month>he.URL_ULTIMO_AÑO_MES[1]:
            break
        url_específico=he.URL_RAIZ+f"{year}/{str(month).zfill(2)}"
        print("fuente:",url_específico, month, he.EXTENSION)
        for file in listFD(url_específico, he.EXTENSION):
            print(file)
            response = requests.get(file)
            local_file_name = file.split("/")[-1]
            local_file_name = DIRECTORIO_I + "\\"+local_file_name
            print(file,"--->",local_file_name)
            with open(local_file_name,"wb") as f:
                f.write(response.content)

