from bs4 import BeautifulSoup
import requests
import time
from time import sleep

bitcoin = 'https://coinmarketcap.com/currencies/bitcoin/'
r = requests.get(bitcoin)
soup = BeautifulSoup(r.text, 'html.parser')
text = soup.find_all('div', {'class':"priceValue"})

ethereum = 'https://coinmarketcap.com/currencies/ethereum/'
r2 = requests.get(ethereum)
soup2 = BeautifulSoup(r2.text, 'html.parser')
text2 = soup2.find_all('div', {'class':"priceValue"})

xrp = 'https://coinmarketcap.com/currencies/xrp/'
r3 = requests.get(xrp)
soup3 = BeautifulSoup(r3.text, 'html.parser')
text3 = soup3.find_all('div', {'class':"priceValue"})

def bitcoin_price():
    for elem in text:
        print("Todays Bitcoin Price Is: " + elem.get_text())
        sleep(2)
        exit()
        
def  ethereum_price():
    for elem in text2:
        print("Todays Ethereum Price is: " + elem.get_text())
        sleep(2)
        exit()
        
def xrp_price():
    for elem in text3:
        print("Todays XRP Price Is: " + elem.get_text())
        sleep(2)
        exit()
        
print("Price Searcher For Crypto V1")
print("............................")
print("What Do You Want To Know The Price Of, Today?")
print("1. Bitcoin")
print("2. Ethereum")
print("3. Ripple XRP")
user_input = input("> ")

if (user_input == '1'):
    bitcoin_price()
    
elif (user_input == '2'):
    ethereum_price()
    
elif(user_input == '3'):
    xrp_price()
    
else:
    print("Wrong Input! Please Try Again...")
    sleep(2)
    exit()