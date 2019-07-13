<!-- name:George
email:276227382@qq.com
date:20190712
introduce:mysql-mongodb汇总比较
env:python3.5 -->
mysql-mongodb汇总比较

1.关系型数据库与非关系型数据库的优缺点
    关系型数据库：
    　　优点：容易理解，逻辑类似常见的表格
    　　　　　　　使用方便，都使用sql语句，sql语句非常成熟
    　　　　　　　数据一致性高，冗余低，数据完整性好，便于操作
    　　　　　　　技术成熟，功能强大，支持很多复杂操作
    　　缺点：每次操作都要进行sql语句解析，消耗较大
           不能很好的满足并发需求，特别是海量数据爆发，关系型数据库读写能力会显得不足
           关系型数据库往往每一步都要进行加锁的操作，也造成了数据库的负担
           数据一致性高，有时也会使数据的存储不灵活
    非关系型数据库(NoSql)
      优点：高并发，读写能力强
      　　　　　弱化数据结构一致性，使用更加灵活
      　　　　　有良好的可扩展性
      缺点：通用性差，没有sql语句那样同于的语句
      　　　　　操作灵活导致容易出错和混乱
      　　　　　没有外键关系等复杂的操作
    NoSql的使用情况：
    １．对数据存储灵活性要求高，一致性要求低
    ２．数据处理海量并发，要求瞬间效率速度比较高
    ３．数据比较容易建立Nosql模型
    ４．网站临时缓冲存储，爬虫应用
    MongoDB数据库的特点:
    1.是由c++编写的数据库管理系统
    ２．支持丰富的数据操作，增删改查索引聚合
    ３．支持丰富的数据类型
    ４．使用方便，可以很好的扩展，相对比较成熟
    ５．支持众多的编程语言接口(python PHP c++ c#)

2.mongodb安装方法
    自动安装:sudo apt-get install mongodb
    　　　　　　　　/var/lib/mongodb(默认安装位置)
            /etc/mongodb.conf(配置文件位置)
            /usr/bin    /usr/local/bin(命令集)
    手动安装:www.mongodb.com(下载安装包)
            /usr/local  /opt(解压安装包)
            以下两句写入启动脚本 /etc/rc.local
            PATH=$PAHT:/opt/mongo...../bin
            export PATH
            重启

3.存储位置

4.mysql 和 mongodb　概念对比
    mysql        mongodb         含义
    database     database       数据库
    table        collection     表/集合
    column       field          字段/域
    row          document       记录/文档
    index        index          索引

5.数据库备份和恢复
    mongodb备份:mongodump -h host -d dbname -o bak
        et: mongodump -h 127.0.0.1 -d test -o bak
    mongodb恢复:mongorestore -h dbhost:port -d dbname path
        et: mongorestore -h 127.0.0.1:27017 -d res bak/test
    mysql备份:mysqldump -u用户名 -p源库名 > ~/***.sql
        源库名:  --all-databases 备份所有库
             　　　　　　　　　　　　　　　　　库名　　　备份单个库
             　　　　　　　　-B 库1 库2 库3  备份多个库
             　　　　　　　　库名　　表1　表2　表3　备份指定库的多张表
        et:mysqldump -uroot -p -all-databases > all.sql
    mysql恢复:mysql -uroot -p 目标库名 < ***.sql
        et:mysql -uroot -p --one-database db4 < all.sql

6.mongobd查找操作,删除操作，修改操作
    查找操作:find(query,field)
    查找操作符:比较　$eq  $lt  $lte  $gt  $gte $ne  $in  $nin
              逻辑 $and $or $not $nor
              数组 $all $size $slice
              其他 $exists $mod $type
    查找函数:pretty()  limit()  skip()  sort()  count() dictinct()
    删除操作:remove(query,justOne)
          et:remove({sex:'w'},true) #true只删除一条
    修改操作:update(query,update,upsert,multi)
            et:db.class.update({age:{$lt:17}},{$set:{age:18}},false,true)
    修改操作符：$set $unset $rename $setOnInsert $inc $mul $min $max
    数组修改器:$push $pushAll $pull $pullAll $each $position $sort $pop
              $addToSet 

7.mongo时间数据类型
    new Date()   Date()   ISODate()   valueOf()
    e.g.
       db.class2.insert({book:'Python入门',date:new Date()})
       db.class2.insert({book:'Python精通',date:ISODate()})

8.mongo索引
    复合索引　　　唯一索引　　　　稀疏索引
    ensureIndex()    dropIndex()   dropIndexes()  getIndexes()
    e.g.
        db.class.ensureIndex({name:1,age:-1},{name:'name_age'})　
        db.class.ensureIndex({name:1},{unique:true})
        db.class.ensureIndex({age:1},{sparse:true})(稀疏索引/间隙索引)

9.mongo聚合操作
    db.class.aggregate()
    $group --->$sum  $avg  $min   $max
        et:db.class.aggregate({$group:{_id:'$gender',max:{$max:'$age'}_}})
    $project(同find函数field格式一样)
        et:db.class.aggregate({$project:{_id:0,name:1,age:1_}})
    $match(同query一致)
        et:db.class.aggregate({$match:{age:{$lt:8}}})
    $limit
        et:db.class.aggregate({$limit:3})
    $skip
        et:db.class.aggregate({$skip:3})
    $sort
        et:db.class.aggregate({$lsort:{age:1}})
    聚合管道：group-->match-->project-->sort

10.mongodb固定集合
    使用：临时缓冲／日志处理
    db.createCollection(collection,{capped:true,size:10000,max:1000})
    capped:true  表示创建固定集合  size:集合的大小字节　　max:文档上限
    e.g.
        db.createCollection(log,{capped:true,size:1000,max:3})

11.mongodb文件存储－－－通过命令行  和　　mysql　下的数据导入与导出
    1.mongodb存储文件路径
        e.g.  
            db.log.insert({filename:'test.mp4',size:247.8,path:'/home/tarena/mongodb/test.mp4'})

   2.mongodb存储文件本身(将文件以二进制存储到数据库中)－－－GridFS存储大文件</p>
        在mongodb中以两个集合配合的方法存储文件
        fs.files:存储文件相关信息（文件名，文件类型）
        fs.chunks:分块存储文件实际内容
            存储文件：mongofiles -d dbname put file
            e.g.
               mongofiles -d grid put test.mp4
            提取文件：mongofiles -d dbname get file
            e.g.
               mongofiles -d grid get test.mp4
   3.mysql下的数据导入
     语法：load data infile "/var/lib/mysql-files/文件名" 
        into table 表名 
        fields terminated by '分隔符' 
        lines terminated by '\n';
     步骤:1.在数据库中创建对应的表 2.把文件拷贝到数据库的默认搜索路径中　3.执行数据导入语句
     　　　　show variables like 'secure_file_priv' 查看默认搜索路径
   4.mysql下的数据导出
       语法: select ... from 表名
       　　　　　　into outfile '/var/lib/mysql-file/文件名'
             fields terminated by '分隔符'
             lines terminated by '\n';

12.mongodb--->python---->pymongo模块
    1.创建mongodb的数据库连接对象
       conn = pymongo.MongoClient('localhost',27017)
    2.生成数据库对象
       db = conn.stu  或者  db = conn['stu']
    3.生成集合对象
       myset = db.class0  或者　myset = db['class0']
    4.集合操作(增删改查索引聚合)
    　　　插入：insert()  insert_many() insert_one() save()
       查找：find() find_one()
            cursor对象:next()  limit() skip() count() sort()
        修改:update update_many() update_one()
        删除：remove()
        索引：ensure_index() list_indexes() drop_index() drop_indexes()
        聚合：update()
    5.关闭数据库连接
       conn.close()

13.mysql --->python---->pymysql模块
　　　　1.建立数据库连接
　　　　　　　　　db = pymysql.connect(host,port,user,password,database,charset)
　　　　2.创建游标对象
         c = db.cursor()
　　　　3.游标方法
         c.execute(sql)
    4.提交到数据库
         db.commit()
    5.关闭游标对象
         c.close()
    6.断开数据库连接
         db.close()

