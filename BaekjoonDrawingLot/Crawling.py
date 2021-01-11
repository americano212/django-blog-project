import requests
from bs4 import BeautifulSoup

session=requests.session()

url  = 'https://www.acmicpc.net/signin'

data={
    "login_user_id": "wq0212",
    "login_password": "qqww0212",

}

response=session.post(url, data=data )

response.raise_for_status()

url="https://www.acmicpc.net/group/practice/4963/44"
response=session.get(url)
response.raise_for_status()

soup=BeautifulSoup(response.text,"html.parser")
print(soup)
