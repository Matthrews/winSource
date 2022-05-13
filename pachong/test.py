import requests

# response = requests.get("http://tiqu.linksocket.com:81/abroad?num=1&type=2&lb=1&sb=0&flow=1&regions=&port=1&n=0")
# ip = response.json()["data"][0]["ip"]
# port = response.json()["data"][0]["port"]
ip = '101.35.141.230'
port = '8888'
ip = "{}:{}".format(ip, port)
print(ip)
proxies = {
    "http": "http://{}".format(ip),
    "https": "https://{}".format(ip),
}

ttt = requests.get("http://myip.top", proxies=proxies)
print(ttt.text)