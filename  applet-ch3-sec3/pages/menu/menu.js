// pages/menu/menu.js

const app = getApp()

const cookieUtil = require('../../utils/cookie.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    grids: null, // 九宫格内容
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.updateMenuData()
  },

  /**
   * 请求后台，更新menu数据
   */
  updateMenuData: function () {
    console.log(app.globalData.auth.isAuthorized)
    // 获取对象
    var that = this;
    if (!app.globalData.auth.isAuthorized) {
      wx.request({
        url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/menu/list',
        header: {
          'content-type': 'application/json' // 默认值
        },

        success(res) {
          var menu_data = res.data.data
          console.log(menu_data)
          // 配置数据
          that.setData({
            grids: menu_data,
          })
        }
      })
    } else {
      console.log('1111111111')
      var cookie = cookieUtil.getCookieFromStorage()
      var header = {}
      header.Cookie = cookie
      wx.request({
        url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/menu/user',
        header: header,
        success(res) {
          var menu_data = []
          console.log(res.data.data)
          if (res.data.data) {
            menu_data = res.data.data
          } else {
            wx.showToast({
              title: '用户暂无应用，请点击添加！',
              icon: 'none'
            })
          }
          // 配置数据
          that.setData({
            grids: menu_data,
          })
        }
      })
    }
  },

  onNavigatorTap: function (e) {
    var index = e.currentTarget.dataset.index
    var item = this.data.grids[index]
    console.log(item)
    if (item.application == 'weather') {
      console.log('-------------')
      wx.navigateTo({
        url: '../weather/weather',
      })
    } else if (item.application == 'backup-image') {
      wx.navigateTo({
        url: '../backup/backup',
      })
    } else if (item.application == 'stock') {
      wx.navigateTo({
        url: '../stock/stock'
      })
    } else if (item.application == 'joke') {
      wx.navigateTo({
        url: '../service/service?type=joke'
      })
    } else if (item.application == 'constellation') {
      wx.navigateTo({
        url: '../service/service?type=constellation',
      })
    }
  },

  moreApp: function () {
    console.log('moreApp')
    if (!app.globalData.auth.isAuthorized) {
      wx.showToast({
        title: '请先登录',
        icon: 'none'
      })
      return
    }
    wx.navigateTo({
      url: '../applist/applist?userMenu=' + JSON.stringify(this.data.grids),
    })
  },

  onPullDownRefresh: function () {
    wx.showLoading({
      title: '加载中',
    })
    this.updateMenuData()
    wx.hideLoading()
  }
})