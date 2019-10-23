

import pymysql

# 连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='test',
                   charset='utf8')
# 生成游标对象(操作数据库，执行sql语句)
cur=db.cursor()

# 存储图片
with open('hg.jpeg','rb') as f:
    data=f.read()

try:
    sql="insert into image values(1,%s,%s);"
    cur.execute(sql,['hg.jpeg',data])
    db.commit()
except Exception as e:
    db.rollback()#事务回滚
    print(e)

# 执行各种对数据库的读写操作



# 关闭游标和数据库连接
cur.close()
db.close()

