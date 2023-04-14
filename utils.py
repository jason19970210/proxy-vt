import requests
from bs4 import BeautifulSoup
import config



def get_proxies_list() -> list:
    proxies_list = []
    for i in config.proxy_websites_list:
        if i == "https://www.sslproxies.org/":
            proxies_list += parser_sslproxies()

    return proxies_list


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
    test_proxy_list(get_proxies_list())