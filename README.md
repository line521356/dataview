# dataview

## git init
## git add
## git commit -m 'msg'
## git push

# 1.熟练使用git，clone代码
# 2.找出明显不合理地方进行修改，修改完提交到github上
# 3.完成上次作业

# mysql
## ddl
### 数据库操作
#### 创建数据库 create database 数据库名
#### 创建数据库如果不存在 create database if not exists 数据库名
#### 创建数据库时设置字符集 create database 数据库名称 character set 字符集名
#### 删除数据库 drop database 数据库名 
#### use
#### select database()

### 数据表的操作
#### 表的创建
create table my_table (
 ‘locID’ INT AUTO_INCREMENT,
 ‘x_position’ FLOAT NOT NULL,
 ‘y_position’ FLOAT NOT NULL,
 ‘z_position’ FLOAT NOT NULL,
 PRIMARY KEY (‘locID’)
);
#### 表的修改
##### alter
###### 修改表名 alter table my_table rename to mytable;
###### desc 查看表结构
###### 表结构修改

## dml
### insert into mytable (x_position, y_position, z_position) values (4353,3453,564356);
### delete from mytable where x_position > 3
### update mytable set y_position=100 where z_position > 4

## dql
## 学生信息 课程信息 教师信息 成绩信息


```sql
create table student(
    id int auto_increment,
    `name` varchar(20) NOT NULL DEFAULT '',
    stu_no varchar(20) not null DEFAULT '',
    gender varchar(10) not null DEFAULT '',
    primary key (id)
);
```
```sql
create table course(
    id int auto_increment,
    `name` varchar(20) NOT NULL DEFAULT '',
    teacher_id int NOT NULL ,
    primary key (id)
);
```
```sql
create table teacher(
    id int auto_increment,
    `name` varchar(20) not null default '',
    primary key (id)
);
```
```sql
create table score(
    id int auto_increment,
    stu_id int not null,
    course_id int not null ,
    num double not null ,
    primary key (id)
);
```

```sql
select stu_no # 需要展示的字段名
from student # 表名
where name='自强'; # 条件

```

```sql
insert into student (id, name, stu_no, gender)
values  (1, '轩昂', '2023001', 'M'),
        (2, '冷峰', '2023002', 'F'),
        (3, '辰阳', '2023003', 'M'),
        (4, '英纵', '2023004', 'F'),
        (5, '翰飞', '2023005', 'M'),
        (6, '涵阳', '2023006', 'F'),
        (7, '墨池', '2023007', 'M'),
        (8, '力臣', '2023008', 'F'),
        (9, '浩淼', '2023009', 'M'),
        (10, '自强', '2023010', 'F'),
        (11, '锋文', '2023011', 'M'),
        (12, '法灿', '2023012', 'F'),
        (13, '天哲', '2023013', 'M'),
        (14, '矾豫', '2023014', 'F'),
        (15, '鸿光', '2023015', 'M'),
        (16, '远航', '2023016', 'F'),
        (17, '嘉瑞', '2023017', 'M'),
        (18, '齐峰', '2023018', 'F'),
        (19, '清平', '2023019', 'M'),
        (20, '智明', '2023020', 'F'),
        (21, '汐梓', '2023021', 'M'),
        (22, '俊颖', '2023022', 'F'),
        (23, '兮筱', '2023023', 'M'),
        (24, '媱倩', '2023024', 'F'),
        (25, '卿菲', '2023025', 'M'),
        (26, '煊悦', '2023026', 'F'),
        (27, '颜英', '2023027', 'M'),
        (28, '觅珞', '2023028', 'F'),
        (29, '云倩', '2023029', 'M'),
        (30, '婷伊', '2023030', 'F'),
        (31, '思瑶', '2023031', 'M'),
        (32, '曦婧', '2023032', 'F'),
        (33, '燕琳', '2023033', 'M'),
        (34, '维茹', '2023034', 'F'),
        (35, '琳欣', '2023035', 'M');
```
```sql
insert into teacher (id, name)
values  (1, '张三'),
        (2, '李四'),
        (3, '王五'),
        (4, '赵六');
```

```sql
insert into course (id, name, teacher_id)
values  (1, '操作系统原理', 1),
        (2, '数据结构', 3),
        (3, '计算机组成原理', 4),
        (4, '计算机网络', 2),
        (5, 'gre', 1),
        (6, '微积分', 1),
        (7, '线性代数', 3);
```


```sql
 insert into score (stu_id, course_id, num) VALUES (1,7,28.25051926);
 insert into score (stu_id, course_id, num) VALUES (1,6,84.13893375);
 insert into score (stu_id, course_id, num) VALUES (1,5,95.09308432);
 insert into score (stu_id, course_id, num) VALUES (1,4,13.81717708);
 insert into score (stu_id, course_id, num) VALUES (1,3,80.02832546);
 insert into score (stu_id, course_id, num) VALUES (1,2,42.03388983);
 insert into score (stu_id, course_id, num) VALUES (1,1,43.54093551);
 insert into score (stu_id, course_id, num) VALUES (2,7,91.78023747);
 insert into score (stu_id, course_id, num) VALUES (2,6,72.45266146);
 insert into score (stu_id, course_id, num) VALUES (2,5,39.55867981);
 insert into score (stu_id, course_id, num) VALUES (2,4,51.83843089);
 insert into score (stu_id, course_id, num) VALUES (2,3,90.64220156);
 insert into score (stu_id, course_id, num) VALUES (2,2,32.74163507);
 insert into score (stu_id, course_id, num) VALUES (2,1,74.45561743);
 insert into score (stu_id, course_id, num) VALUES (3,7,83.22491567);
 insert into score (stu_id, course_id, num) VALUES (3,6,69.39997306);
 insert into score (stu_id, course_id, num) VALUES (3,5,48.42080493);
 insert into score (stu_id, course_id, num) VALUES (3,4,78.64017915);
 insert into score (stu_id, course_id, num) VALUES (3,3,60.75378604);
 insert into score (stu_id, course_id, num) VALUES (3,2,29.83174201);
 insert into score (stu_id, course_id, num) VALUES (3,1,50.43801298);
 insert into score (stu_id, course_id, num) VALUES (4,7,14.15821615);
 insert into score (stu_id, course_id, num) VALUES (4,6,34.56925238);
 insert into score (stu_id, course_id, num) VALUES (4,5,84.54815006);
 insert into score (stu_id, course_id, num) VALUES (4,4,32.74222945);
 insert into score (stu_id, course_id, num) VALUES (4,3,80.55461055);
 insert into score (stu_id, course_id, num) VALUES (4,2,22.65263261);
 insert into score (stu_id, course_id, num) VALUES (4,1,87.22298101);
 insert into score (stu_id, course_id, num) VALUES (5,7,6.755028962);
 insert into score (stu_id, course_id, num) VALUES (5,6,79.92227716);
 insert into score (stu_id, course_id, num) VALUES (5,5,70.16762016);
 insert into score (stu_id, course_id, num) VALUES (5,4,79.11123308);
 insert into score (stu_id, course_id, num) VALUES (5,3,11.0517126);
 insert into score (stu_id, course_id, num) VALUES (5,2,40.94462948);
 insert into score (stu_id, course_id, num) VALUES (5,1,51.38758499);
 insert into score (stu_id, course_id, num) VALUES (6,7,99.64249062);
 insert into score (stu_id, course_id, num) VALUES (6,6,68.29416064);
 insert into score (stu_id, course_id, num) VALUES (6,5,56.34015245);
 insert into score (stu_id, course_id, num) VALUES (6,4,95.32605273);
 insert into score (stu_id, course_id, num) VALUES (6,3,37.12399249);
 insert into score (stu_id, course_id, num) VALUES (6,2,68.32462145);
 insert into score (stu_id, course_id, num) VALUES (6,1,38.25554168);
 insert into score (stu_id, course_id, num) VALUES (7,7,39.55691206);
 insert into score (stu_id, course_id, num) VALUES (7,6,96.01719741);
 insert into score (stu_id, course_id, num) VALUES (7,5,42.25524835);
 insert into score (stu_id, course_id, num) VALUES (7,4,22.65222172);
 insert into score (stu_id, course_id, num) VALUES (7,3,91.79043039);
 insert into score (stu_id, course_id, num) VALUES (7,2,94.47916883);
 insert into score (stu_id, course_id, num) VALUES (7,1,5.147230756);
 insert into score (stu_id, course_id, num) VALUES (8,7,95.28932324);
 insert into score (stu_id, course_id, num) VALUES (8,6,65.1345768);
 insert into score (stu_id, course_id, num) VALUES (8,5,25.04651498);
 insert into score (stu_id, course_id, num) VALUES (8,4,93.15066749);
 insert into score (stu_id, course_id, num) VALUES (8,3,70.16850867);
 insert into score (stu_id, course_id, num) VALUES (8,2,18.27084485);
 insert into score (stu_id, course_id, num) VALUES (8,1,32.72870695);
 insert into score (stu_id, course_id, num) VALUES (9,7,16.04711901);
 insert into score (stu_id, course_id, num) VALUES (9,6,32.93114991);
 insert into score (stu_id, course_id, num) VALUES (9,5,19.85027156);
 insert into score (stu_id, course_id, num) VALUES (9,4,14.15919931);
 insert into score (stu_id, course_id, num) VALUES (9,3,58.97799844);
 insert into score (stu_id, course_id, num) VALUES (9,2,48.42035733);
 insert into score (stu_id, course_id, num) VALUES (9,1,71.19116095);
 insert into score (stu_id, course_id, num) VALUES (10,7,96.52971288);
 insert into score (stu_id, course_id, num) VALUES (10,6,8.824764472);
 insert into score (stu_id, course_id, num) VALUES (10,5,94.22811272);
 insert into score (stu_id, course_id, num) VALUES (10,4,72.7090394);
 insert into score (stu_id, course_id, num) VALUES (10,3,81.58432447);
 insert into score (stu_id, course_id, num) VALUES (10,2,70.16902695);
 insert into score (stu_id, course_id, num) VALUES (10,1,38.7658127);
 insert into score (stu_id, course_id, num) VALUES (11,7,53.93436866);
 insert into score (stu_id, course_id, num) VALUES (11,6,69.39763814);
 insert into score (stu_id, course_id, num) VALUES (11,5,71.09071395);
 insert into score (stu_id, course_id, num) VALUES (11,4,23.87058881);
 insert into score (stu_id, course_id, num) VALUES (11,3,82.35020997);
 insert into score (stu_id, course_id, num) VALUES (11,2,13.48584855);
 insert into score (stu_id, course_id, num) VALUES (11,1,72.45291998);
 insert into score (stu_id, course_id, num) VALUES (12,7,95.09441346);
 insert into score (stu_id, course_id, num) VALUES (12,6,2.674458735);
 insert into score (stu_id, course_id, num) VALUES (12,5,95.45187086);
 insert into score (stu_id, course_id, num) VALUES (12,4,0.756162901);
 insert into score (stu_id, course_id, num) VALUES (12,3,28.11322395);
 insert into score (stu_id, course_id, num) VALUES (12,2,38.23874756);
 insert into score (stu_id, course_id, num) VALUES (12,1,40.7183091);
 insert into score (stu_id, course_id, num) VALUES (13,7,8.825025901);
 insert into score (stu_id, course_id, num) VALUES (13,6,5.146917789);
 insert into score (stu_id, course_id, num) VALUES (13,5,96.52911381);
 insert into score (stu_id, course_id, num) VALUES (13,4,46.22178049);
 insert into score (stu_id, course_id, num) VALUES (13,3,33.33171774);
 insert into score (stu_id, course_id, num) VALUES (13,2,95.32691189);
 insert into score (stu_id, course_id, num) VALUES (13,1,3.292230608);
 insert into score (stu_id, course_id, num) VALUES (14,7,51.4346953);
 insert into score (stu_id, course_id, num) VALUES (14,6,90.64190386);
 insert into score (stu_id, course_id, num) VALUES (14,5,44.51237014);
 insert into score (stu_id, course_id, num) VALUES (14,4,66.69814648);
 insert into score (stu_id, course_id, num) VALUES (14,3,0.067307402);
 insert into score (stu_id, course_id, num) VALUES (14,2,45.01848424);
 insert into score (stu_id, course_id, num) VALUES (14,1,93.83105011);
 insert into score (stu_id, course_id, num) VALUES (15,7,77.30079344);
 insert into score (stu_id, course_id, num) VALUES (15,6,68.74025228);
 insert into score (stu_id, course_id, num) VALUES (15,5,68.32406918);
 insert into score (stu_id, course_id, num) VALUES (15,4,89.56079494);
 insert into score (stu_id, course_id, num) VALUES (15,3,61.10457274);
 insert into score (stu_id, course_id, num) VALUES (15,2,44.24045746);
 insert into score (stu_id, course_id, num) VALUES (15,1,82.34880877);
 insert into score (stu_id, course_id, num) VALUES (16,7,39.98973344);
 insert into score (stu_id, course_id, num) VALUES (16,6,34.56798046);
 insert into score (stu_id, course_id, num) VALUES (16,5,37.81587416);
 insert into score (stu_id, course_id, num) VALUES (16,4,72.45435114);
 insert into score (stu_id, course_id, num) VALUES (16,3,95.28941033);
 insert into score (stu_id, course_id, num) VALUES (16,2,24.25329393);
 insert into score (stu_id, course_id, num) VALUES (16,1,28.25116822);
 insert into score (stu_id, course_id, num) VALUES (17,7,19.85105079);
 insert into score (stu_id, course_id, num) VALUES (17,6,40.94400423);
 insert into score (stu_id, course_id, num) VALUES (17,5,89.18423477);
 insert into score (stu_id, course_id, num) VALUES (17,4,21.84428828);
 insert into score (stu_id, course_id, num) VALUES (17,3,65.13492199);
 insert into score (stu_id, course_id, num) VALUES (17,2,53.93526937);
 insert into score (stu_id, course_id, num) VALUES (17,1,82.87545198);
 insert into score (stu_id, course_id, num) VALUES (18,7,28.25294645);
 insert into score (stu_id, course_id, num) VALUES (18,6,38.23933234);
 insert into score (stu_id, course_id, num) VALUES (18,5,55.47415682);
 insert into score (stu_id, course_id, num) VALUES (18,4,93.41688529);
 insert into score (stu_id, course_id, num) VALUES (18,3,25.0467024);
 insert into score (stu_id, course_id, num) VALUES (18,2,40.94387235);
 insert into score (stu_id, course_id, num) VALUES (18,1,60.4524923);
 insert into score (stu_id, course_id, num) VALUES (19,7,22.70409089);
 insert into score (stu_id, course_id, num) VALUES (19,6,39.9884658);
 insert into score (stu_id, course_id, num) VALUES (19,5,63.23289147);
 insert into score (stu_id, course_id, num) VALUES (19,4,14.1579466);
 insert into score (stu_id, course_id, num) VALUES (19,3,62.93666825);
 insert into score (stu_id, course_id, num) VALUES (19,2,93.83029701);
 insert into score (stu_id, course_id, num) VALUES (19,1,59.3969174);
 insert into score (stu_id, course_id, num) VALUES (20,7,1.737866137);
 insert into score (stu_id, course_id, num) VALUES (20,6,46.22051204);
 insert into score (stu_id, course_id, num) VALUES (20,5,45.85966156);
 insert into score (stu_id, course_id, num) VALUES (20,4,37.98411889);
 insert into score (stu_id, course_id, num) VALUES (20,3,78.79580088);
 insert into score (stu_id, course_id, num) VALUES (20,2,82.87533594);
 insert into score (stu_id, course_id, num) VALUES (20,1,59.39888856);
 insert into score (stu_id, course_id, num) VALUES (21,7,68.77822351);
 insert into score (stu_id, course_id, num) VALUES (21,6,94.47717858);
 insert into score (stu_id, course_id, num) VALUES (21,5,31.7983098);
 insert into score (stu_id, course_id, num) VALUES (21,4,93.4169486);
 insert into score (stu_id, course_id, num) VALUES (21,3,94.22666545);
 insert into score (stu_id, course_id, num) VALUES (21,2,58.00442458);
 insert into score (stu_id, course_id, num) VALUES (21,1,89.2361856);
 insert into score (stu_id, course_id, num) VALUES (22,7,77.298666);
 insert into score (stu_id, course_id, num) VALUES (22,6,34.3661364);
 insert into score (stu_id, course_id, num) VALUES (22,5,92.14457915);
 insert into score (stu_id, course_id, num) VALUES (22,4,89.18200201);
 insert into score (stu_id, course_id, num) VALUES (22,3,94.34693481);
 insert into score (stu_id, course_id, num) VALUES (22,2,95.32510011);
 insert into score (stu_id, course_id, num) VALUES (22,1,95.29042382);
 insert into score (stu_id, course_id, num) VALUES (23,7,44.29750827);
 insert into score (stu_id, course_id, num) VALUES (23,6,32.72869987);
 insert into score (stu_id, course_id, num) VALUES (23,5,94.34681458);
 insert into score (stu_id, course_id, num) VALUES (23,4,84.54832237);
 insert into score (stu_id, course_id, num) VALUES (23,3,19.85079111);
 insert into score (stu_id, course_id, num) VALUES (23,2,94.47900675);
 insert into score (stu_id, course_id, num) VALUES (23,1,68.73781891);
 insert into score (stu_id, course_id, num) VALUES (24,7,49.43916569);
 insert into score (stu_id, course_id, num) VALUES (24,6,45.85952003);
 insert into score (stu_id, course_id, num) VALUES (24,5,44.23906253);
 insert into score (stu_id, course_id, num) VALUES (24,4,60.75262161);
 insert into score (stu_id, course_id, num) VALUES (24,3,93.41443996);
 insert into score (stu_id, course_id, num) VALUES (24,2,71.68249915);
 insert into score (stu_id, course_id, num) VALUES (24,1,34.56842481);
 insert into score (stu_id, course_id, num) VALUES (25,7,59.76030146);
 insert into score (stu_id, course_id, num) VALUES (25,6,33.33218137);
 insert into score (stu_id, course_id, num) VALUES (25,5,33.09909713);
 insert into score (stu_id, course_id, num) VALUES (25,4,79.11309883);
 insert into score (stu_id, course_id, num) VALUES (25,3,85.48148001);
 insert into score (stu_id, course_id, num) VALUES (25,2,81.58554856);
 insert into score (stu_id, course_id, num) VALUES (25,1,69.69544551);
 insert into score (stu_id, course_id, num) VALUES (26,7,54.90220842);
 insert into score (stu_id, course_id, num) VALUES (26,6,40.71881385);
 insert into score (stu_id, course_id, num) VALUES (26,5,18.79669437);
 insert into score (stu_id, course_id, num) VALUES (26,4,93.83160523);
 insert into score (stu_id, course_id, num) VALUES (26,3,13.48779131);
 insert into score (stu_id, course_id, num) VALUES (26,2,56.33795119);
 insert into score (stu_id, course_id, num) VALUES (26,1,60.4536484);
 insert into score (stu_id, course_id, num) VALUES (27,7,25.0478947);
 insert into score (stu_id, course_id, num) VALUES (27,6,61.10457578);
 insert into score (stu_id, course_id, num) VALUES (27,5,98.51179853);
 insert into score (stu_id, course_id, num) VALUES (27,4,94.34763994);
 insert into score (stu_id, course_id, num) VALUES (27,3,63.48873478);
 insert into score (stu_id, course_id, num) VALUES (27,2,92.27239562);
 insert into score (stu_id, course_id, num) VALUES (27,1,8.825395974);
 insert into score (stu_id, course_id, num) VALUES (28,7,58.76163773);
 insert into score (stu_id, course_id, num) VALUES (28,6,95.45138952);
 insert into score (stu_id, course_id, num) VALUES (28,5,23.8617881);
 insert into score (stu_id, course_id, num) VALUES (28,4,46.22064774);
 insert into score (stu_id, course_id, num) VALUES (28,3,78.59377737);
 insert into score (stu_id, course_id, num) VALUES (28,2,22.70431042);
 insert into score (stu_id, course_id, num) VALUES (28,1,17.09854084);
 insert into score (stu_id, course_id, num) VALUES (29,7,6.971168672);
 insert into score (stu_id, course_id, num) VALUES (29,6,21.84447049);
 insert into score (stu_id, course_id, num) VALUES (29,5,33.14930641);
 insert into score (stu_id, course_id, num) VALUES (29,4,69.39902769);
 insert into score (stu_id, course_id, num) VALUES (29,3,49.31184422);
 insert into score (stu_id, course_id, num) VALUES (29,2,79.92176218);
 insert into score (stu_id, course_id, num) VALUES (29,1,89.05258395);
 insert into score (stu_id, course_id, num) VALUES (30,7,58.76255188);
 insert into score (stu_id, course_id, num) VALUES (30,6,20.83008087);
 insert into score (stu_id, course_id, num) VALUES (30,5,18.26807355);
 insert into score (stu_id, course_id, num) VALUES (30,4,34.36685774);
 insert into score (stu_id, course_id, num) VALUES (30,3,62.1331885);
 insert into score (stu_id, course_id, num) VALUES (30,2,82.35035736);
 insert into score (stu_id, course_id, num) VALUES (30,1,19.38797486);
 insert into score (stu_id, course_id, num) VALUES (31,7,53.7001362);
 insert into score (stu_id, course_id, num) VALUES (31,6,81.98856411);
 insert into score (stu_id, course_id, num) VALUES (31,5,54.94410822);
 insert into score (stu_id, course_id, num) VALUES (31,4,6.376478082);
 insert into score (stu_id, course_id, num) VALUES (31,3,61.5684822);
 insert into score (stu_id, course_id, num) VALUES (31,2,9.864368428);
 insert into score (stu_id, course_id, num) VALUES (31,1,28.11557908);
 insert into score (stu_id, course_id, num) VALUES (32,7,68.77840505);
 insert into score (stu_id, course_id, num) VALUES (32,6,63.23483433);
 insert into score (stu_id, course_id, num) VALUES (32,5,38.23983677);
 insert into score (stu_id, course_id, num) VALUES (32,4,69.69575226);
 insert into score (stu_id, course_id, num) VALUES (32,3,40.71933514);
 insert into score (stu_id, course_id, num) VALUES (32,2,10.11617274);
 insert into score (stu_id, course_id, num) VALUES (32,1,47.65939531);
 insert into score (stu_id, course_id, num) VALUES (33,7,78.63928882);
 insert into score (stu_id, course_id, num) VALUES (33,6,98.51261045);
 insert into score (stu_id, course_id, num) VALUES (33,5,73.854347);
 insert into score (stu_id, course_id, num) VALUES (33,4,21.6795722);
 insert into score (stu_id, course_id, num) VALUES (33,3,21.90016157);
 insert into score (stu_id, course_id, num) VALUES (33,2,87.22337678);
 insert into score (stu_id, course_id, num) VALUES (33,1,70.36521225);
 insert into score (stu_id, course_id, num) VALUES (34,7,0.34037082);
 insert into score (stu_id, course_id, num) VALUES (34,6,59.87069758);
 insert into score (stu_id, course_id, num) VALUES (34,5,89.23543979);
 insert into score (stu_id, course_id, num) VALUES (34,4,97.07479844);
 insert into score (stu_id, course_id, num) VALUES (34,3,31.20161821);
 insert into score (stu_id, course_id, num) VALUES (34,2,80.4785987);
 insert into score (stu_id, course_id, num) VALUES (34,1,37.36831997);
 insert into score (stu_id, course_id, num) VALUES (35,7,53.69878905);
 insert into score (stu_id, course_id, num) VALUES (35,6,92.17405469);
 insert into score (stu_id, course_id, num) VALUES (35,5,63.48616461);
 insert into score (stu_id, course_id, num) VALUES (35,4,86.16999655);
 insert into score (stu_id, course_id, num) VALUES (35,3,4.401954012);
 insert into score (stu_id, course_id, num) VALUES (35,2,6.770727205);
 insert into score (stu_id, course_id, num) VALUES (35,1,21.18665198);
```
# 作业要求
1. 查询每个老师所带的课
```sql
SELECT teacher.name, course.name, teacher.id, teacher_id
FROM teacher, course;
```
2. 给student score表插入一行数据
```sql
insert into score (stu_id, course_id, num) VALUES (35,1,100);
```
3. 查询每门课的最高分（max()）
```sql
SELECT course_id,MAX(num)
FROM score GROUP BY course_id;
```
4. 查询每门课的平均分
```sql
SELECT course_id, AVG(num)
FROM score GROUP BY course_id;
```
5. 查询所有学生的每门课的平均分 
```sql
SELECT course_id, AVG(num)
FROM score GROUP BY course_id;
```
6. 查询各科前五名（多条sql查询）
```sql
select a.id, a.stu_id, a.course_id, a.num from score a
where exists
    (select count(*) from score where course_id = a.course_id and num>a.num having count(*)<5)
order by a.course_id, num desc;
```
7. 查询《线性代数》大于60分的学生
```sql
SSELECT 
    stu_id, course_id, num
From score
inner join course c on score.course_id = c.id
where name='线性代数' and num>60;
```
8. 查询科目平均分小于60分的学生
```sql
SELECT
    stu_id
FROM score
GROUP BY stu_id
HAVING avg(num)>60;
```

9. 查询学生名，课程名，对应成绩导出csv，使用python统计每个学生的科目平均分
```sql
mysql -hxxx -uxx -pxx
SELECT stu_id, course_id, num from score into outfile 'stu_score.csv'
```