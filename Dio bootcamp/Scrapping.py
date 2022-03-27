from bs4 import BeautifulSoup

import requests


site = requests.get("https://www.climatempo.com.br/").content
