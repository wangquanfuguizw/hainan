import requests
import re

url = "http://www.hnftp.gov.cn/xxgk/dsj/"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Referer': 'http://www.hnftp.gov.cn/yshj/zdcy/',
  'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
  'Cookie': 'H0EONiMfekeDS=5wNmzShUwQPIvVhIomJyUt1rjGOxdRWr02hUbVSL_dmTOZsNGrLxHtoWdeQJuv2wlZSDOt4oD02zU4gtLYePNRG; enable_H0EONiMfekeD=true'
}

response = requests.request("GET", url, headers=headers, data=payload)
response.encoding = 'utf8'

print(response.text)
