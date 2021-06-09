import requests
from bs4 import BeautifulSoup

def htmlparse(url):
    #網站的request請求
    r=requests.get(url)
    r.encoding='utf-8'
    #html分析
    html_doc=r.text
    soup=BeautifulSoup(html_doc,'html.parser')

    return soup