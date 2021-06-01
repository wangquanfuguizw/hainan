# import requests
# kv = {
#     'authToken': 'b003ca05f3e6a60fbdda7f4d8ad04c6c',
#     'BGQ': 20160000
#       }
# r = requests.get('http://data.hainan.gov.cn//api/invoke/1828341116a34865ac2a6267a98a6664', params = kv)

import re
import urllib.request
from bs4 import BeautifulSoup
import xlwt

def main():
    baseurl = 'http://data.hainan.gov.cn//api/invoke/1828341116a34865ac2a6267a98a6664?BGQ=20160000&authToken=b003ca05f3e6a60fbdda7f4d8ad04c6c'
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = '豆瓣电影Top250.xls'

    #askURL('http://data.hainan.gov.cn//api/invoke/1828341116a34865ac2a6267a98a6664?authToken=b003ca05f3e6a60fbdda7f4d8ad04c6c&BGQ=')
    #3.保存数据

findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) #re.S让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

def getData(baseurl):
    datalist = []
    for i in range(2010,2016):
        url = baseurl + str(i*10000)
        html = askURL(url)      #保存获取到的网页源码
        #2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        # for item in soup.find_all('div', class_="item"):
        #     data = [] #保存一部电影的所有信息
        #     item = str(item)
        #
        #     link = re.findall(findLink, item)[0] #re库用来通过正则表达式查找指定的字符串
        #     data.append(link)
        #     imgSrc = re.findall(findImgSrc, item)[0]
        #     data.append(imgSrc)
        #     titles = re.findall(findTitle, item)
        #     if(len(titles) == 2):
        #         ctitle = titles[0]
        #         data.append(ctitle)
        #         otitle = titles[1].replace("/", "") #去掉无关的符号
        #         data.append(otitle)
        #     else:
        #         data.append(titles[0])
        #         data.append(' ')
        #     rating = re.findall(findRating, item)[0]
        #     data.append(rating)
        #
        #     judgeNum = re.findall(findJudge, item)[0]
        #     data.append(judgeNum)
        #
        #     inq = re.findall(findInq, item)
        #     if len(inq) != 0:
        #         inq = inq[0].replace('。', '.')
        #         data.append(inq)
        #     else:
        #         data.append(' ')
        #
        #     bd = re.findall(findBd, item)[0]
        #     bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)
        #     bd = re.sub('/', ' ', bd)
        #     data.append(bd.strip())   #去掉前后的空格
        #
        #     datalist.append(data)

    #print(datalist)
    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Cookie": "UM_distinctid=178d5c179a614a-0ecad5064390ca-3f356b-144000-178d5c179a7822; yfx_c_g_u_id_10005682=_ck21041521385013251557955492237; Hm_lvt_b23dcf9fcb01d857002fb0a0edee33b3=1618493930; _trs_uv=knixkurl_4505_9hgk; H0EONiMfekeDS=5eQY8bXpnnG8FCnkD_5XQRU.fop6LMdzAT370gpRedfq_wWUZ8.9A5JGGHuLOi5BfN11.OCzBKYmmpqtOCYjluq; yfx_f_l_v_t_10005682=f_t_1618493930324__r_t_1619179244736__v_t_1619179244736__r_c_1; Hm_lpvt_b23dcf9fcb01d857002fb0a0edee33b3=1619180325; H0EONiMfekeDT=53xEXtCc1hjWqqqmyinvSna1ODa8tXIQr3q6FocZzIt72ii_uKofFT.63Hanf5qBjFEFFXBkuPgGl1rG8o9pgIHDzD_e_t4bdLvP4cy4FXW4CrhCYjYF14iM9JtUAkVws6RrqMxsLaMyCWb61cc5fmfvwV1Ss1D2jv.UnuXISE1IDpRXjGMdiJ1FIjVh_pZoAF3jtP0r9lTw9jQcPSfApJNO7YNjWkSAFLHxy0Dj6rkIMdRr2bCjmAp_sY9rV8uorXhuJeHey6txqydBMgoGMCr4aUPd3OohhK.bqRzABihNmAkhxn90qxm508lVMIKlaLbk7j657p9uQLJpfuCvEO5",
        "Host": "data.hainan.gov.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": 1
    } # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return html

if __name__ == '__main__':
    main()
    print('爬取完毕')