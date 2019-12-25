// pages/weather/weather.js

const app = getApp()

const popularCities = [{
    "province": "广东省",
    "city": "深圳市",
    "area": "南山区"
  },
  {
    "province": "广东省",
    "city": "广州市",
    "area": "天河区"
  },
  {
    "province": "北京市",
    "city": "北京市",
    "area": "朝阳区"
  },
  {
    "province": "上海市",
    "city": "上海市",
    "area": "徐汇区"
  }
]

Page({

  // 页面的初始数据
  data: {
    isAuthorized: false,
    weatherData: null
  },

  onLoad: function(options) {
    // 页面加载时，就调用函数，更新天气
    this.updateWeatherData()
  },

  updateWeatherData: function() {
    var that = this
    wx.request({
      url:app.globalData.serverUrl + app.globalData.apiVersion + '/service/weather',
      method: 'POST',
      data: {
        // 后台是根据POST中的cities属性来获得城市列表的
        cities: popularCities
      },
      success: function(res){
        var tmpData = res.data.data
        that.setData({
          // 将取出的数据放入data数据的weatherData中
          weatherData: tmpData
        })
      }
    })
  },


  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {
    this.updateWeatherData()
  }
})