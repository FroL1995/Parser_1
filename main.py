import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://snaryazhenie-patronov.ru/russia/korolev/'
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find_all("div", class_="product-block product-thumb")
    print(spoon)

    # part = soup.find("div", class_="text-container")
    # with open("page.txt", 'a', encoding='UTF-8') as file:
    #     file.write(part.text)


if __name__ == '__main__':
    main()