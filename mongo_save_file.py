#小文件存储方案
#直接转换为二进制格式插入到数据库

from pymongo import MongoClient
import bson.binary

#创建数据库连接
conn = MongoClient('localhost',27017)
#创建image数据库对象
db = conn.image
#创建ABC集合对象
myset = db.logo


# #1.存储文件
# f = open('logo.png','rb')

# #将文件内容转化为可存储的二进制格式
# content = bson.binary.Binary(f.read())

# #插入到文档
# myset.insert({'filename':'logo.png','data':content})


#2.提取文件
img = myset.find_one({'filename':'logo.png'})

#将内容写入到本地
with open('logo.png','wb') as f:
    f.write(img['data'])

conn.close()

