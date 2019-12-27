// pages/stock/stock.js

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    stockData: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.updataStockData()
  },

  updataStockData: function(){
    var that = this
    wx.showLoading({
      title: '数据加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/stock',
      success: function(res){
        that.setData({
          stockData: res.data.data
        })
        // 请求成功后，隐藏提示信息
        wx.hideLoading()
      },
      fail: function(res){
        console.log('fail')
      }
    })
  },

})