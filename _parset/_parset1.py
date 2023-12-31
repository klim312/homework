from bs4 import BeautifulSoup as BS
import requests


HEADERS ={
    'Aсcept_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7.'
}


def get_url():
    url = f"https://www.mashina.kg/"

    return url


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="pl-item-wrapper", limit=5)
    wheels = []

    for item in items:
        wheels.append({
            "url": f"https://www.mashina.kg/{item.find('a').get('href')}",
            "title": item.find("div", class_="pl-item-info-expandable").find("a").getText(),
            "price": item.find("div", class_="price-wrapper").find("span").getText()

        })
    return wheels


def parser():
    url = get_url()
    html = get_html(url)
    data = get_data(html.text)
    return data


parser()
