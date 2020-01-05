# encoding: utf-8
"""实现类似API proxy的功能"""
import logging
import datetime

from thirdparty import juhe
from thirdparty.weather import heweather, CommonWeatherResult

logger = logging.getLogger('django')

__author__ = "bbw"


class WeatherAPIProxy:
    @classmethod
    def ha_request(cls, cityname, timeout):
        """
        :param cityname:
        :param timeout:利用该参数判断请求是否发生故障
        :return:
        """
        try:
            data = juhe.weather(cityname, timeout)
        except Exception as e:
            # 如果发生异常就说明是请求超时了，便去请求heweather的数据
            logger.error("Request juhe weather API timeout. "
                         "HARequest switch to hefeng weather.")
            data = heweather.HeWeather.get_weather(cityname, timeout)
            return data


if __name__ == "__main__":
    print(WeatherAPIProxy.ha_request('北京', 1))
