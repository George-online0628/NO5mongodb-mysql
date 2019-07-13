# 数据库增删改查操作
from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost',27017)

# 创建数据库对象
db = conn.grade

#创建集合对象
myset = db.class4

#插入数据操作
# myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':'张国立','King':'康熙'},\
#     {'name':'陈道明','King':'康熙'}])
# myset.insert_many([{'name':'唐国强','King':'雍正'},\
#     {'name':'陈建斌','King':'雍正'}])
# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.save({'_id':1,'name':'聂远','King':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})


#查找操作
# cursor = myset.find({},{'_id':0})  #find()得到字典对象

# for i in cursor:
#     print(i['name'],'----',i['King'])

# dic = myset.find_one({},{'_id':0})　　#find_one()得到一条数据
# print(dic)


#操作符操作
myset1 = db.class1

# cursor = myset1.find({'age':{'$gt':10}},{'_id':0})
# # for i in cursor:
# #     print(i)

# #获取下一条数据
# print(cursor.next())
# print(cursor.next())

# cursor1 = myset1.find({},{'_id':0})
# for i in cursor1.sort([('age',1)]):
#     print(i)

# query = {'$or':[{'gender':'w'},{'age':{'$lt':19}}]}
# cursor = myset1.find(query,{'_id':0})
# for i in cursor:
#     print(i)


#修改
# myset1.update({'name':'CC'},{'$unset':{'hobby':''}})

#同时修改多条文档
myset1.update({'name':'DD'},{'$set:{'age':12}'},multi = True)

#如果匹配文档不存在则插入
myset.update({'name':'梁家辉'},{'$set':{'King':'咸丰'}},upsert = True)


#删除

myset.remove({'King':'四爷'})
#只删除一个符合条件的文档
myset.remove({'King':'咸丰'},multi = False)
myset1.remove({'gender':{'$exists':False}})

#复操操作
print(myset.find_one_and_delete({'King':'咸丰'}))

#关闭连接
conn.close()
