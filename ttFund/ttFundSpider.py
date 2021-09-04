import requests
import time
import re

class ttFundSpider:
    def request(self,page):
        dt = int(round(time.time() * 1000 ))
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&" \
              "page={0},200&dt={1}&atfc=&onlySale=0".format(page,dt)
        
        heads = {
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
            }
        
        response = requests.get(url,headers = heads)
        self.convertStr2List(response.text)
        
    def convertStr2List(self,resText):
        pattern = re.compile(r"datas:(.*),count")
        resStr = pattern.search(resText).group(1)
        resStr = re.sub(r"\[",'',resStr)
        resStr = re.sub(r"\]",'',resStr)
        resStrList = resStr.split(',')
        result = []
        tmpList = []
        i = 0
        
        for resStr in resStrList:
            tmpList.append(resStr)
            i = i + 1
            if i % 21 == 0:
                result.append(tmpList)
                tmpList = []
        
        print('2List:',result)
        
        
if __name__ =='__main__':
    ttSpider = ttFundSpider()
    for page in range(1,3):
        print('spider page{0}--'.format(page))
        ttSpider.request(page)