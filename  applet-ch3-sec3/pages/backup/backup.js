// pages/backup/backup.js
const app = getApp()
const imageUrl = app.globalData.serverUrl + app.globalData.apiVersion + '/service/image'

Page({
  data: {
    // 需要上传的图片
    needUploadFiles: [],
    // backupedFiles每个元素四个字段 name, md5, path, isDownloaded
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

  onLoad: function() {
    this.downloadAllFromRemote()
  },

  // 下载所有的已备份图片
  downloadAllFromRemote: function () {
    var that = this
    wx.request({
      url: imageUrl + '/list',
      method: 'GET',
      success: function (res) {
        var imageList = res.data.data
        for (var i = 0; i < imageList.length; i++) {
          var imageItem = imageList[i]
          that.downloadFile(imageItem)
        }
      }
    })
  },
  
  // 长按确认函数
  longTapConfirm: function(e){
    var that = this
    var confirmList = ["删除备份"]
    wx.showActionSheet({
      itemList: confirmList,
      success: function(res){
        if(res.cancel){
          // 如果用户选择的取消，就返回
          return
        }
        // 本地图片的删除
        var imageIndex = e.currentTarget.dataset.index  // 取出前端传入的data-index，图片序号
        var imageItem = that.data.downloadedBackupedFiles[imageIndex]
        var newList = that.data.downloadedBackupedFiles
        newList.splice(imageIndex, 1)  // 将获得到的这个数组移除掉  
        that.setData({
          downloadedBackupedFiles: newList
        })
        console.log(imageItem)
        // 远端图片的删除
        that.deleteBackup(imageItem)
      }
    })
  },

  //上传图片文件
  uploadFiles: function(){
    var that = this
    that.setData({
      newBackupedFiles: []
    })
    for (var i=0; i<this.data.needUploadFiles.length; i++){
      var file = this.data.needUploadFiles[i]
      wx.uploadFile({
        url: imageUrl,
        filePath: file,
        name: 'test',
        success: function (res) {
          var res = JSON.parse(res.data)
          var md5 = res.data[0].md5
          var name = res.data[0].name
          var newImageItem = {
            "md5": md5,
            "name": name
          }
          // 上传成功后，自动刷新图片
          that.downloadFile(newImageItem)
        }
      })
    }
    wx.showToast({
      title: '上传成功',
    })
    this.setData({
      needUploadFiles: []
    })
  },

  // 下载图片
  downloadFile: function(imgItem){
    var that = this
    var downloadUrl = imageUrl + '?md5=' + imgItem.md5
    wx.downloadFile({
      url: downloadUrl,
      success: function(res) {
        var filepath = res.tempFilePath
        console.log(filepath)
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        imgItem.path = filepath
        // 操作图片数组，向数组开头添加一个或多个元素，返回新的长度
        newDownloadedBackupedFiles.unshift(imgItem)
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles
        })
        console.log(newDownloadedBackupedFiles)
      }
    })
  },

  // 删除图片
  deleteBackup: function(imgItem){
    console.log('delete a backup file:' + imgItem)
    wx.request({
      url: imageUrl + '?md5=' + imgItem.md5,
      method: 'DELETE',
      success: function(res){
        console.log(res)
        wx.showToast({
          title: '删除成功',
        })    
      },
    })
  }
});