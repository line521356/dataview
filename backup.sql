# select  teacher_id,sum(id) from course group by teacher_id #having count(*) > 1
# 聚合函数 reduce map
# 查询每门课学号最大的学生的成绩
# select * from student s,(select max(st.stu_no) max_no from student st)  st_max_no
# where s.stu_no = st_max_no.max_no

select
    c.id,s.stu_no,s.name,sc.num
from score sc, student s,course c,(select max(st.stu_no) max_no from student st)  st_max_no
where sc.stu_id = s.id
and sc.course_id = c.id
and s.stu_no = st_max_no.max_no
group by c.id,s.stu_no,s.name,sc.num

# 查询teacher_id 重复的
select
    *
from
    course c1,
    (select c.teacher_id from course c group by c.teacher_id having count(*) >1) c2
where c1.teacher_id = c2.teacher_id

# case when then
select
    s.id as '主键',
    s.stu_id as '学生表主键',
    case
        when s.num >=60
        then '及格'
        when s.num < 60
        then '不及格'
    end as '是否及格'
from
    score s


select  concat(concat(s.name,' '),s.stu_no) from student  s