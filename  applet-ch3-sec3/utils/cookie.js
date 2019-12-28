const key = 'cookie'

function getSessionIDFromResponse(res){
  // 负责从Response取出cookies
  var cookie = res.header['Set-Cookie']  // 返回头部的关键字Set-Cookie取出cookie
  console.log('get cookie from response: ' + cookie)
  return cookie
}

function setCookieToStorage(cookie){
  // 负责将cookies存储到storage中
  try{
    wx.setStorageSync(key, cookie)
  }catch(e){
    console.log(e)
  }
}

function getCookieFromStorage() {
  // 负责将cookies从stroage取出
  var value = wx.getStorageSync(key)
  return value
}

// 导出三个函数，在外部直接调用
module.exports = {
  setCookieToStorage: setCookieToStorage,
  getCookieFromStorage: getCookieFromStorage,
  getSessionIDFromResponse: getSessionIDFromResponse
}
