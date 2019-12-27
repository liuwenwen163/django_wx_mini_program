// pages/service/service.js

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    isConstellationView: false,
    isJokeView: false,
    constellationData: null,
    jokeData: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    var isConstellationViewTmp = false
    var isJokeViewTmp = false
    if(options.type == 'constellation'){
      // 如果是con，就将星座的标志位设置为true，调用星座的函数
      isConstellationViewTmp = true
      this.updateConstellationData()
    }else if (options.type == 'joke') {
      // 如果是joke，原理同上
      isJokeViewTmp = true
      this.updateJokeData()
    }
    this.setData({
      isConstellationView: isConstellationViewTmp,
      isJokeView: isJokeViewTmp
    })
  },

  updateConstellationData: function() {
    var that = this
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/constellation',
      success: function (res) {
        that.setData({
          constellationData: res.data.data
        })
        // 请求成功后，隐藏提示信息
        wx.hideLoading()
      },
    })
  },

  updateJokeData: function () {
    var that = this
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/joke',
      success: function(res) {
        that.setData({
          jokeData: res.data.data
        })
        wx.hideLoading()
      }
    })
  },
})