from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import app.WeatherCrawler as WC
import json
# Create your views here.

def index(request):
    data = {
        'title': [
            '海南地图',
            '地区经济',
            '热门景区',
            '景点热搜',
            '游客散点图',
            '大事记',
            '词频分析'
        ]
    }
    return render(request, 'index.html', {'result': data})

def weather(request):
    if request.method == "POST":
        req = request.POST.get('name')
        #print(req)
        date = WC.select(req)
        mes = {
            'title': [
                req,
                '天气预警',
                '当地气温',
                '每小时天气',
                '污染成分',
                '生活',
                '天气预报'
            ]
        }
        return JsonResponse({"status": "200", "message": date, "result": mes})
    else:
        data = {
            'title': '1111'
        }
        return render(request, 'detail.html', {'result': data})