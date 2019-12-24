// pages/menu/menu.js

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    grids: [{
      "name": "应用1"
    }, {
      "name": "应用2"
    }], // 九宫格内容
  },

  /**
   * 生命周期函数--监听页面加载，
   * 当页面加载时，调用updateMenu函数页面
   */
  onLoad: function (options) {
    this.updateMenuData()
  },

  /**
   * 请求后台，更新menu的数据
   */
  updateMenuData: function () {
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})