import requests
import json
from web3 import Web3
from web3.auto import w3
from bs4 import BeautifulSoup
import os
while True:
    r = requests.get('https://arbiscan.io/txsDeposits')
    soup = BeautifulSoup(r.content,"lxml")
    al = soup.find("tbody")
    rows = al.find('tr')
    rows1 = rows.find_all("td")
    rows2 = rows1[5]

    for a in rows2.find_all('a', class_="hash-tag text-truncate"):
        True

    linko = a["href"]
    linko1 = linko.split("tx/")
    linko1 = linko1[1]
    kontrol_et = open("bune.txt","r")
    kontrol = kontrol_et.read()
    kontrol_et.close()
    if kontrol == linko1 :
        True
    else :
        url = "infura-link"
        web3 = Web3(Web3.HTTPProvider(url))

        den = web3.eth.get_transaction(f'{linko1}')
        den = str(den)
        den1 = den.find("to': ")
        listRes = list(den.split(" "))
        contract = listRes[29].replace("'","").replace(",","")
        from1 = listRes[9].replace("'","").replace(",","")
        
        if from1.startswith("0x"):
            mevcut_dizin = os.getcwd()
            os.listdir(mevcut_dizin)
            if f"{contract}.txt" in os.listdir(mevcut_dizin):
                True
            else :
                yazma = open(f"{contract}.txt","w")
                yazma.close() 
            deneme_1 = open(f"{contract}.txt","r")
            if f'{from1}' in deneme_1.read():
                False
            else :
                deneme_2 = open("bune.txt","w")
                deneme_2.write(linko1)
                deneme_2.close()
                deneme_3 = open(f"{contract}.txt","a") 
                deneme_3.write(f"{from1}\n") 
                deneme_3.close()                   
        else :
            contract = listRes[21].replace("'","").replace(",","")
            from1 = listRes[5].replace("'","").replace(",","") 

            deneme_4 = open(f"{contract}.txt","r")
            if f'{from1}' in deneme_4.read():
                False
            else :
                deneme_5 = open("bune.txt","w")
                deneme_5.write(linko1)
                deneme_5.close()
                deneme_6 = open(f"{contract}.txt","a")
                deneme_6.write(f"{from1}\n")   
                deneme_6.close() 
            deneme_4.close()                           
  


