import pymysql
sql='/*--user=root;--password=123456;--host=192.168.1.5;--execute=1;--port=3306;--enable-ignore-warnings=1;*/\
inception_magic_start;\
use test;\
insert into t_backup values(5);\
insert into t_backup values(6);\
insert into t_backup values(7);\
insert into t_backup values(8);\
delete from t_backup where id = 8;\
inception_magic_commit;'
try:
    conn=pymysql.connect(host='192.168.1.6', user='', passwd='', db='', port=6669)
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description)
    print(result)
    field_names = [i[0] for i in cur.description]
    # for row in result:
    #     print(row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",
    #     row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10])
    cur.close()
    conn.close()
except Exception as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))