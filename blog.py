import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def buscar_enlaces(soup, url, dominio_base):
    enlaces = set()
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        url_completa = urljoin(url, href)
        if urlparse(url_completa).netloc == dominio_base:
            enlaces.add(url_completa)
    return enlaces

def buscar_URJC(texto):
    expresion = r"\bURJC\b"
    return len(re.findall(expresion, texto))

def buscar_webs(url_original):
    dominio = urlparse(url_original).netloc
    urls_no_visitadas = {url_original}
    urls_visitadas = set()
    coincidencias = 0
    while urls_no_visitadas:
        url = urls_no_visitadas.pop()
        if url not in urls_visitadas:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    texto = soup.get_text()
                    coincidencias += buscar_URJC(texto)
                    print(coincidencias)
                    enlaces = buscar_enlaces(soup, url, dominio)
                    for enlace in enlaces:
                        if enlace not in urls_visitadas:
                            urls_no_visitadas.add(enlace)
                    urls_visitadas.add(url)
            except requests.RequestException:
                continue
    return coincidencias

url = "https://r2-ctf-vulnerable.numa.host/"
total_pal = buscar_webs(url)
print(total_pal)