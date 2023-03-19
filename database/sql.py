import pymysql

conn = pymysql.connect(host="127.0.0.1",user="root",password="",database="school",charset="utf8")
cur = conn.cursor()
# cur.execute("select * from course")
# all = cur.fetchall()
# for item in all:
#     print(item)
cur.execute("insert into course (`name`,`teacher_id`) values ('拓扑学','3')")
a = 1/0
cur.execute("insert into course (`name`,`teacher_id`) values ('信息论','3')")
conn.commit()