import requests
import urllib.request, socket
from bs4 import BeautifulSoup
import config
import time

socket.setdefaulttimeout(10)

def get_proxies_list() -> list:
    proxies_list = []
    for i in config.proxy_websites_list:
        if i == "https://www.sslproxies.org/":
            proxies_list += parser_sslproxies()

    return proxies_list

def test_proxy(proxy: str) -> bool:
    try:
        proxy_handler = urllib.request.ProxyHandler({'https': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        sock=urllib.request.urlopen('https://www.google.com/')  # change the url address here
        return True

    except urllib.error.HTTPError as e:
        return e

    except Exception as detail:
        return detail



def test_proxy_list(proxies_list: list) -> list:
    valid_proxies_list = [ i for i in proxies_list if ... ]
    print(valid_proxies_list)


def parser_sslproxies() -> list:

    res = requests.get('https://www.sslproxies.org/')
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')

        filter = 'elite proxy'
        """
        leave blank for disable filter
        values: 'elite proxy', 'anonymous', ''
        """

        # filter = ''
        if len(filter):
            return [ f"{tags[0].text}:{tags[1].text}" for tags in [ td[0].find_all('td')[:2] for td in [ [tr] for tr in soup.find('table').find_all('tr')[1:] ] if td[0].find_all('td')[4].text == filter ] ]

        return [ f"{tags[0].text}:{tags[1].text}" for tags in [ td[0].find_all('td')[:2] for td in [ [tr] for tr in soup.find('table').find_all('tr')[1:] ] ] ]


if __name__ == '__main__':
    # test_proxy_list(get_proxies_list())
    while 1:
        print(test_proxy('200.105.215.22:33630'))
        time.sleep(2)