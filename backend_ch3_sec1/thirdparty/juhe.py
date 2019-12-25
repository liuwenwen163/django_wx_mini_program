# encoding: utf-8
import json
import requests


__author__ = "bbw"


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = '7036a6c0ecd2a4dc39fe08779f4b0b20'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)
    result = json_data.get('result')
    sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('temp')
    response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('wind_strength')
    response['humidity'] = sk.get('humidity')  # 湿度
    response['time'] = sk.get('time')
    return response

if __name__ == '__main__':
    data = weather('深圳')
