const db = wx.cloud.database()   //1.初始化数据库

function getMacData(machine){
  return db.collection(machine)
}

module.exports = {
  db:db,
  getMacData:getMacData
}
