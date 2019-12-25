// pages/backup/backup.js
const app = getApp()
const imageUrl = app.globalData.serverUrl + app.globalData.apiVersion + '/service/image'

Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 需要上传的图片
    needUploadFiles: [],
    // 已下载的备份图片
    downloadedBackupedFiles: [],
  },

  // 绑定前台的点击上传的函数
  chooseImage: function(e){
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 指定是原图上传还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function(res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          // 将图片路径存入该属性
          needUploadFiles: that.data.needUploadFiles.concat(res.tempFilePaths)
        });
      },
    })
  },

  // 上传图片文件
  uploadFiles: function(imgItem){
    // uploadFiles会调用chooseImage函数
    for (var i=0; i<this.data.needUploadFiles.length; i++){
      // 迭代对象的每个元素都是一个文件路径
      var filePath = this.data.needUploadFiles[i]
      wx.uploadFile({
        // imageUrl是上面拼接好的常量
        url: imageUrl,
        filePath: filePath,
        name: 'test',
        // res是后端返回的返回值
        success: function(res){
          console.log(res)
        }
      })
    }
  },

  // 下载图片
  downloadFile: function(imgItem){
    var that = this
    wx.downloadFile({
      url: imageUrl + '?md5=' + 'c272fb65f82896887eaf7d99bf90856d',
      success: function(res){
        var tempPath = res.tempFilePath
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        newDownloadedBackupedFiles.push(tempPath)
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles
        })
      }
    })
  },

  // 删除图片
  deleteBackup: function(imgItem){
    wx.request({
      url: imageUrl + '?md5=' + 'c272fb65f82896887eaf7d99bf90856d',
      method: 'DELETE',
      success: function(res){
        console.log(res.data)
        wx.showToast({
          title: '删除成功',
        })
      }
    })
  }
})