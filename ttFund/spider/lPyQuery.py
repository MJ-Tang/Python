import requests
from pyquery import PyQuery as pg

url = "https://cn.investing.com/equities/baidu.com"

heads = {
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
            }

response = requests.get(url,headers = heads)

doc = pg(response.text)
price = doc("#last_last")