import pyautogui as pag
import time
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

table = pd.read_csv("produtos.csv")
print(table)

pag.PAUSE = 0.6
pag.FAILSAFE = True

def open_link():
    pag.press("win")
    pag.write("chrome")
    pag.press("enter")
    pag.write(link)
    pag.press("enter")
    time.sleep(3)

open_link()

def login_on_site():
    pag.click(734, 374) # Alterar esse valor de acordo com a tela utilizando o arquivo auxiliar.py
    pag.write(email)
    pag.press("tab")
    pag.write(password)
    pag.press("enter")
    time.sleep(4)

login_on_site()

def post_product():
    #itera sobre cada linha e índice da tabela
    for index, row in table.iterrows():
        pag.click(730, 259) #alterar o valor de acordo com a tela
        try:
            #itera sobre os campos da tabela e caso ele exista escreve o valor do campo
            for field in row:
                if pd.notna(field):
                    pag.write(str(field))

                pag.press("tab")
            pag.press("enter")
            pag.scroll(5000)
        except:   
            print(f"Erro na linha {index}")

            #feito mais enxuto com loops para não precisar criar manualmente
            #for linha in tabela.index:
                #codigo = str(tabela.loc[field, "codigo"])
                #pag.write(codigo)
                #pag.press("tab")
                #marca = str(tabela.loc[field, "marca"])
                #pag.write(marca)
                #pag.press("tab")
post_product()

    



