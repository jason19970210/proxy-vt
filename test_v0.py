import requests
import time
# from random import randint

url = "https://www.virustotal.com/ui/search?query=da3dbd2b3028344a7"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept-Ianguage": "en-US,en;q=0.9,es;q=0.8",
    "X-Tool": "2",
    "X-VT-Anti-Abuse-Header": "2"
}

s = requests.Session()
s.proxies = {
    "http": "102.33.149.99:8088",
    "http": "102.213.87.14:8080",
    "http": "102.165.51.172:3128",
    "http": "103.101.82.106:80"
}

i = 0
while 1:
    res = s.get(url=url, headers=headers, timeout=1)
    if res.status_code == 200:
        i += 1
    else:
        print(res.status_code)
        break

print(i)