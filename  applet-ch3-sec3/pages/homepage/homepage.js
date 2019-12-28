// pages/homepage/homepage.js

const app = getApp()
const cookieUtil = require('../../utils/cookie.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  onReadCookies: function () {
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/auth/test',
      success(res) {
        var cookie = cookieUtil.getSessionIDFromResponse(res)
        console.log(cookie)
        cookieUtil.setCookieToStorage(cookie)


        // 将cookie存储到storage中
        var newCookie = cookieUtil.getCookieFromStorage()  // 从storage中取出cookie
        var header = {}
        header.Cookie = newCookie
        wx.request({
          url: app.globalData.serverUrl + app.globalData.apiVersion + '/auth/test2',
          header: header,  // 将有cookie的头传入
          success: function (res) {

          }
        })
      }
    }
    )
  },

  authorize: function () {
    wx.login({  // 调用wx.login()
      success: function (res) {
        var code = res.code  // 获取临时的code
        var appId = app.globalData.appId
        var nickname = app.globalData.userInfo.nickName
        wx.request({
          url: app.globalData.serverUrl + app.globalData.apiVersion + '/auth/authorize',
          method: 'POST',
          data: {  // 将要验证的数据发送到后台
            code: code,
            appId: appId,
            nickname: nickname
          },
          header: {
            'content-type': 'application/json'
          },
          success: function (res) {
            wx.showToast({
              title: '授权成功'
            })
            var cookie = cookieUtil.getSessionIDFromResponse(res)
            cookieUtil.setCookieToStorage(cookie)
            console.log(cookie)
          }
        })
      }
    })
  }
})