import requests
import time
import json


def getCity():
    url = 'http://cdn.weather.hao.360.cn/sed_api_area_query.php?grade=city&_jsonp=loadCity2&code=31&_=1620820680344'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }
    try:
        res = requests.get(url, headers=header)
        res.raise_for_status()
        res.encoding = 'utf-8'
        text = res.text[11:]
        return json.loads(text[:-2])
    except Exception as e:
        print(e)


def getW(code):
    timestamp = int(time.time() * 1000)
    t = timestamp
    c = timestamp + int(code)
    url = 'http://tq.360.cn/api/weatherquery/querys?app=tq360&code={code}&t={t}&c={c}&_jsonp=renderData'.format(
        code=code, t=t, c=c)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }
    try:
        res = requests.get(url, headers=header)
        res.raise_for_status()
        res.encoding = 'utf-8'
        text = res.text[11:]
        return json.loads(text[:-1])
    except Exception as e:
        print(e)


def start():
    citys = getCity()
    for item in citys:
         cityName = item[0]
         cityCode = item[1]
         cityW = getW('101' + str(cityCode))
         #print(cityName)
    return cityName

def select(name):
    citys = getCity()
    for item in citys:
        cityName = item[0]
        cityCode = item[1]
        cityW = getW('101' + str(cityCode))
        if(name == cityName):
            return cityW

if __name__ == '__main__':
    start()