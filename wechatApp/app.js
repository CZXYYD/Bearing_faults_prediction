//app.js
App({
  onLaunch: function () {
    //初始化云
    wx.cloud.init({
      env:'test-yui',    //环境
      traceUser:true    //是否在console查看用户信息
    })
  },
  globalData: {

  }
})