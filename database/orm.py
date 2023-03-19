import peewee
from peewee import Model, CharField

conn = peewee.MySQLDatabase(host="127.0.0.1",port=3306, user="root", password="", database="school", charset="utf8")
# 元数据
conn.connect()

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = conn

class Course(BaseModel):
    id = peewee.IntegerField()
    name = peewee.CharField()
    teacher_id = peewee.IntegerField()



# course = Course(id=14,name='自动控制',tracher_id=3)
# course.save()
# conn.commit()
# course = Course.create()
# course.name='自动控制'
# course.teacher_id = 3
# course.save()
course = Course.get(id=13)
print(course.name)
print(course.teacher_id)

# 插入两门课程
# 查询数据结构这门课的teacher_id
# 删除线性代数
# 将机器学习的teacher_id修改为2



