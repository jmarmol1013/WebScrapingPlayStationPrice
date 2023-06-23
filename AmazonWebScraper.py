from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import json

def check_price():
    # Connect to website
    URL = 'https://www.amazon.ca/Playstation-3006635-PlayStation-Digital-Edition/dp/B09DFHJTF5/ref=sr_1_4?crid=1171AZAJZJW3A&keywords=playstation+5&qid=1687480973&sprefix=play+station+5%2Caps%2C76&sr=8-4'

    HEADERS = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57",
        "Accept-Encoding":"gzip, deflate", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "DNT":"1",
        "Connection":"close", 
        "Upgrade-Insecure-Requests":"1",
    }

    # Get info from page
    page = requests.get(URL,headers=HEADERS)
    soup1 = BeautifulSoup(page.content,'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    # Get item info
    title = soup2.find(id='productTitle').text.strip()
    price = soup2.find('span', {'class': 'a-offscreen'}).text.strip()[1:]
    date = datetime.date.today()
    
    # Information for CSV
    data = [title,price,date]
    
    # Create CSV
    with open('PlayStationPrices.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    # Send an email if it is lower than $800
    if(float(price) < 700):
        send_email(price,URL)

# Send email with information
def send_email(price,url):
    SMTP_SERVER = 'smtp.gmail.com'
    PORT = 465
    with open('config.json') as config_file:
        config = json.load(config_file)
        ADDRESS = config['email']
        PASSWORD = config['password']

    email_msg = f"""\
    From: {ADDRESS}
    To: {ADDRESS}
    Subject: PLAY STATION PRICE!!

    The Play Station in amazon is lower than $700, price = ${price} in {url}
    """

    try:
        smtp_s = smtplib.SMTP_SSL(SMTP_SERVER,PORT)
        smtp_s.ehlo()
        smtp_s.login(ADDRESS,PASSWORD)
        smtp_s.sendmail(ADDRESS,ADDRESS,email_msg)
    except Exception as e:
        print(f"Issue with sending the email... {e}")
    else:
        print("Email send successfully")
        smtp_s.close()


# Repeat every day
while True:
    check_price()
    time.sleep(86400)
