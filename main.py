#!/usr/bin/env python3
# sudo apt install python3.10-venv chromium-chromedriver feh xvfb --yes
# linux # python3 -m venv lin_venv3104 && . lin_venv3104/bin/activate
# windows # py -m venv win_venv3104
# pip install requests bs4 lxml selenium webdriver_manager
# kill $(pgrep -f .vscode-server/bin/) # убить иксы vscode
# ssh-keygen
# ssh-copy-id vladium@myselfserver
# crontab -e
# @reboot /usr/bin/sleep 15; ssh vladium@myselfserver Xvfb &
# */5 * * * * cd /home/vladium/code/find_mobile/ && /home/vladium/code/find_mobile/lin_venv3104/bin/python3 /home/vladium/code/find_mobile/main.py >> out.log 2>&1
import requests, csv, re, sys, os.path

from bs4 import BeautifulSoup as BS
from time import sleep
from random import uniform
from datetime import datetime

from html_win_selen import get_html_win_selen
from html_lin_selen import get_html_lin_selen
from config import TOKEN, CHAT_ID
from headers import headers



def urls():
    with open("./ulrs.txt") as file:
        return [i.strip() for i in file.readlines()]

def save(data, flag="w"):
    with open('./fm.csv', flag):
        for i in data:
            with open('./fm.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((i['title'], i['price'], i['link']))


def lst_old_result():
    with open('./fm.csv', encoding='utf-8') as file:
        order = ['title', 'price', 'link']
        reader = csv.DictReader(file, fieldnames=order)
        return [i for i in reader]


def get_html(url):
    sleep(uniform(0.1, 0.5))  
    if "lin" in sys.platform:
        response = requests.get(url, headers=headers)
        if response.ok:
            # with open("index.html", "w") as file:
            #     file.write(response.text)
            return response.text
        print("SELENIUM => [ + ]", datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        return get_html_lin_selen(url)
    elif "win" in sys.platform:
        return get_html_win_selen(url)


def gnaw_samsung(avito_title, avito_price, res, link, flag=True):
    lnk = False
    lst_samsung = []
    with open("./samsung.csv") as file:
        for i in file.readlines():
            lst_samsung.append(i.strip().split(","))

    for telephone in lst_samsung:
        re_title = telephone[0]
        standart_price = int(telephone[1])
        min_price = int(telephone[2])

        lst_chars = re.findall(r'[a-zA-Z]+', re_title)
        lst_nums = re.findall(r'\d+', re_title)

        char_one = lst_chars[0]
        if char_one == "a":
            char_one = "(a|а)"
        elif char_one == "m":
            char_one = "(m|м)"

        if lst_nums:
            num_one = lst_nums[0]
            lst_plus = re.findall(r'\++', re_title)
            if lst_plus:
                pattern = fr"{char_one}\s?{num_one}\s?(\+)"
            elif len(lst_chars) > 1:
                char_two = lst_chars[1]
                pattern = fr"{char_one}\s?{num_one}\s?({char_two}(\W|$))"
            else:
                pattern = fr"{char_one}\s?{num_one}\b(?!([ ]?(lite(\W|$)|plus(\W|$)|\+(\W|$)|ultra(\W|$)|e(\W|$)|s(\W|$)|fe(\W|$))))"
        else:
            pattern = fr"[ ]{char_one}(\s|$)"

        if re.search(pattern, avito_title.lower()):
            lnk = True
            if avito_price <= standart_price and avito_price > min_price:
                data = {'title': avito_title, 'price': str(avito_price), 'link': link}
                res.append(data)
    
    if not lnk and flag:
        html = get_html(link)
        soup = BS(html, "lxml")
        new_title = "⮭" + soup.find("ul", class_="params-paramsList-2PiKQ").find_all("li")[2].text.split(":")[1].strip()
        gnaw_samsung(new_title, avito_price, res, link, flag=False)


def gnaw_xiaomi(avito_title, avito_price, res, link, flag=True):
    lnk = False
    lst_xiaomi = []
    with open("./xiaomi.csv") as file:
        for i in file.readlines():
            lst_xiaomi.append(i.strip().split(","))

    for telephone in lst_xiaomi:
        re_title = telephone[0]
        standart_price = int(telephone[1])
        min_price = int(telephone[2])

        lst_chars = re.findall(r'[a-zA-Z]+', re_title)
        lst_nums = re.findall(r'\d+', re_title)

        char_one = lst_chars[0]
        if len(lst_chars) == 2:
            char_two = lst_chars[1]
        if len(lst_chars) == 3:
            char_three = lst_chars[2]

        if lst_nums:
            num_one = lst_nums[0]
            if len(lst_chars) == 3 and "redmi" in lst_chars and "note" in lst_chars:
                pattern = fr"(\s|^){char_one}\s?{char_two}\s{num_one}\s?({char_three}(\W|$))"
            if len(lst_chars) == 3 and "mi" in lst_chars:
                pattern = fr"(\s|^)({char_one}\s?)?{num_one}\s?{char_two}\s{char_three}"
            elif len(lst_chars) == 2 and "redmi" in lst_chars and "note" in lst_chars:
                pattern = fr"(\s|^){char_one}\s{char_two}\s?{num_one}(\s|$)?(?!(\d|[ ][t](\W|$)|[t](\W|$)))"
            elif len(lst_chars) == 2 and "redmi" in lst_chars:
                pattern = fr"(\s|^){char_one}\s?{num_one}\s?{char_two}(\W|$)"
            elif len(lst_chars) == 1 and "redmi" in lst_chars:
                pattern = fr"(\s|^){char_one}\s?{num_one}\s?(?!\d|\s?(a|c)(\W|$)|\s?t(\W|$))"
            elif len(lst_chars) == 2 and "mi" in lst_chars:
                pattern = fr"(\s|^)({char_one}\s?)?{num_one}?\s?{char_two}({num_one})?(\W|$)(?!(\s?(lite|pro|i)))"
            elif len(lst_chars) <= 2:
                pattern = fr"(\s|^)({char_one}\s?)?(?<!note |edmi ){num_one}\s?(?!\d|(\s?(lite|pro|i))|[t](\W|$)|[ ][t](\W|$))"
        else:
            if len(lst_chars) == 2:
                pattern = f"(\s|^)({char_one}\s)?{char_two}(\W|$)"
            elif "poco" in lst_chars:
                pattern = fr"poco"

        if re.search(pattern, avito_title.lower()):
            lnk = True
            if avito_price <= standart_price and avito_price > min_price:
                data = {'title': avito_title, 'price': str(avito_price), 'link': link}
                res.append(data)

    if not lnk and flag:
        # print(f"Ныряем: {avito_title} ==> ", end="")
        html = get_html(link)
        soup = BS(html, "lxml")
        new_title = soup.find("ul", class_="params-paramsList-2PiKQ").find_all("li")[2].text.split(":")[1].strip()
        # print(new_title)
        gnaw_xiaomi(new_title, avito_price, res, link, flag=False)


def get_data(html):
    res = []
    soup = BS(html, 'lxml')
    brand = soup.title.text.split(" ")[4].strip().lower()
    print(brand)
    items = soup.find("div", {"data-marker": "catalog-serp"}).find_all('div', {"data-marker": "item"})

    for item in items:
        try:
            if "items-vipGrid" in str(item.parent).split(">")[0]:
                continue
        except Exception as ex:
            print(f"get_data(): {ex}")
        title = item.find('a', class_='link-link-MbQDP').text
        try:
            price = int(item.find('span', class_='price-text-_YGDY').text.replace('\xa0', '').replace('₽', '').strip())
        except:
            price = 0
        link = 'https://www.avito.ru' + item.find('a', class_='link-link-MbQDP').get('href')

        if brand == "samsung":
            gnaw_samsung(title, price, res, link, flag=True)
        elif brand == "xiaomi":
            gnaw_xiaomi(title, price, res, link, flag=True)
    
    return res


def get_data_pages(url):
    lst_data_pages = []
    for i in range(1, 4):  # проверяем только 3 страницы
        link = f"{url}&p={i}"
        lst_data_pages.extend(get_data(get_html(link)))
    
    return lst_data_pages


def verify_news(url):
    ref_lst = lst_old_result()
    new_lst = get_data(get_html(url))
    freshs_lst = []
    for new in new_lst:
        if new not in ref_lst:
            freshs_lst.append(new)
    if freshs_lst:
        for i in freshs_lst:
            msg = str(i['title'] + '\n' + i['price'] + '\n' + i['link'])
            requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=dict(chat_id=CHAT_ID, text=msg, disable_web_page_preview=True))
        freshs_lst.extend(ref_lst[:50])
        save(freshs_lst)


def main():
    start = datetime.now()
    try:
        if os.path.exists('./fm.csv'):
            for url in urls():
                verify_news(url)
        else:
            for url in urls():
                save(get_data_pages(url), flag="a")
        print("[ + ]", datetime.now().strftime('%d-%m-%Y %H:%M:%S'), end=" ")
    except Exception as ex:
        print(f"[ - ] {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {ex}")
    print(f"time lap: {datetime.now() - start}")


if __name__ == "__main__":
    main()
