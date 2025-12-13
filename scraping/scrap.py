import requests as r
from bs4 import BeautifulSoup

try:
    resultado = r.get("https://www.uol.com.br/")
except Exception as erro:
    print("Erro: ", erro)
else:
    resposta = resultado.text
    soup  = BeautifulSoup(resposta, "html.parser")
    
    print(soup.find("div", class_="cardLive section__grid__main__highlight__item" ).prettify())
    

