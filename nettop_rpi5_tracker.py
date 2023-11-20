from bs4 import BeautifulSoup
import requests

base_url = 'https://nettop.gr/index.php/en/raspberry-pi-en/'
pi5_parts = [
    'kits-and-boards/raspberry-pi-5-8gb',
    'cases/raspberry-pi-5-case-black',
    'accsssories/power-supplies/27w-usb-c-pd-power-supply-black',
    'aksesouar/cooling/raspberry-pi-active-cooler'
]

for item in pi5_parts:
    response = requests.get(f'{base_url}/{item}.html')
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1", {"class": "title"})
    price = soup.find("span", {"class": "PricesalesPrice"})
    stock = soup.select_one("div.stock i")

    print(f'{title.text}:', f'{price.text}\n{base_url}' if 'green' in stock['class'] else f'{stock.text}')
