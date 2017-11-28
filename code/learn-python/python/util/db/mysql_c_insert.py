import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")
#使用cursor()方法获取操作游标
cursor = db.cursor()

#SQL插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
         VALUES('Lily','Greens',20,'F',2000)"""

try:
    #执行SQL语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #Rollback in case there is any error
    db.rollback()

#关闭数据库连接
db.close()