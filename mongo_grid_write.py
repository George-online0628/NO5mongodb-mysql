#将文件以grid方案存放到数据库
from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)

#连接grid数据库
db = conn.grid

#获取gridfs对象
fs = gridfs.GridFS(db)

f = open('ABCmaze.pdf','rb')

#将内容写入到数据库
fs.put(f.read(),filename ='ABCmaze.pdf')

conn.close()
