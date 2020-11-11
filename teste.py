from selenium import webdriver
from time import sleep
import pandas as pd

WPP_LINK = 'https://web.whatsapp.com/'
CHROME_PATH = r'C:\Users\Dell\Downloads\chromedriver.exe'
SEARCH= '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
PRIMEIRO_CONTATO = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div'
TYPE_MSG = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
SEND_BUTTON = '//*[@id="main"]/footer/div[1]/div[3]/button/span'
NEW_MSG = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'

driver = webdriver.Chrome(CHROME_PATH)
driver.get(WPP_LINK)

def new_msg():
    new_msg = driver.find_element_by_xpath(NEW_MSG)
    new_msg.click()
    sleep(2)

def procurar_contato(destinatario):
    search = driver.find_element_by_xpath(SEARCH)
    search.click()
    sleep(2)
    search.send_keys(destinatario)
    sleep(2)
    primeiro = driver.find_element_by_xpath(PRIMEIRO_CONTATO)
    primeiro.click()
    sleep(1)          
    
def enviar_msg(MENSAGEM):
    type_msg = driver.find_element_by_xpath(TYPE_MSG)
    type_msg.click()
    sleep(1)
    type_msg.send_keys(MENSAGEM)
    send= driver.find_element_by_xpath(SEND_BUTTON)
    send.click()
    
df = pd.read_excel("exemplo_excel.xlsx")
nomes_palavras_chaves = df.Contato
lista_mensagens = df.Mensagem

for contato,msg in zip(nomes_palavras_chaves,lista_mensagens):
    new_msg()
    procurar_contato(contato)
    enviar_msg(msg)

print("Mensagens Enviadas")    