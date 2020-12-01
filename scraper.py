#pip install requests
#pip install beautifulsoup4
#coloquei uma frase de teste
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml.etree as xml
#pip install selenium
apt-get update # to update ubuntu to correctly run apt install
apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")
import time

URL = "https://alertalicitacao.com.br/!busca/abertas/telecomunica%C3%A7%C3%A3o+telecomunica%C3%A7%C3%B5es+software+google+arboriza%C3%A7%C3%A3o+mapa+geo+referenciamento+georeferenciamento+frota+mapeamento+posi%C3%A7%C3%A3o+localiza%C3%A7%C3%A3o+fibra+%C3%B3tica"
wd = webdriver.Chrome('chromedriver',options=chrome_options)
wd.get(URL)


r1=wd.page_source
time.sleep(2)
soup=BeautifulSoup(r1,'html.parser')
lista = []
countpag=int(len(soup.select("a[href*='#busca']"))/2)

for i in range(2,countpag+2,1):

  paineis=soup.find_all('div', class_='panel') #lista de elementos bs4: Tags
  for propriedade in paineis:
    titulo = propriedade.find('a', href=True).text
    href = 'https://alertalicitacao.com.br'+ propriedade.a.get('href')
    pos1 = str(propriedade.select('p')[1].text)
    pos2 = str(propriedade.select('p')[2].text)
    pos3 = str(propriedade.select('p')[3].text)
    try:
      pos4 = str(propriedade.select('p')[4].text)
    except:
      pos4 = None
    try:
      pos5 = str(propriedade.select('p')[5].text)
    except:
      pos5 = None
    try:
      pos6 = str(propriedade.select('p')[6].text)
    except:
      pos6 = None
    infosdict = {
        'titulo':titulo,
        'link':href,
        'pos1':pos1,
        'pos2':pos2,
        'pos3':pos3,
        'pos4':pos4,
        'pos5':pos5,
        'pos6':pos6
    }
    lista.append(infosdict)
  time.sleep(3)
  xpath='//*[@id="page-wrapper"]/div/a['+str(i)+']'
  #wd.implicitly_wait(10)
  wd.find_element_by_xpath(xpath).click()
  r1=wd.page_source
  time.sleep(2)
  soup=BeautifulSoup(r1,'html.parser')
  print (xpath)

time.sleep(5)
wd.quit
print(len(lista))
print (lista)
