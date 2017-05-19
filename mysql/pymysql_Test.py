import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', port=3306, charset='utf8')
cur = conn.cursor()
cur.execute("USE mysql")
a=cur.execute("SELECT * FROM help_keyword")
results = cur.fetchall()

for r in results:
    # print 'mail:%s ' % r
    print r
conn.close()