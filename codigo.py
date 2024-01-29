# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=490, y=363)
pyautogui.write("aaaaaaaaaaa@gmail.com")

pyautogui.press("tab")
pyautogui.write("minhasenha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=495, y=248)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)