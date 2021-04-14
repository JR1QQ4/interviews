create table grade
(
    no int auto_increment primary key,
    id    int         not null,
    kemu  varchar(20) not null,
    score int         not null
);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (1, 1001, '语文', 85);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (2, 1001, '数学', 86);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (3, 1002, '英语', 98);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (4, 1002, '语文', 94);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (5, 1002, '数学', 98);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (6, 1003, '数学', 56);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (7, 1003, '语文', 69);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (8, 1003, '英语', 68);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (9, 1004, '英语', 99);
INSERT INTO interview.grade (no, id, kemu, score) VALUES (10, 1004, '数学', 97);

create table student
(
    id   int default 1001 not null primary key,
    name varchar(20)      not null,
    age  int              not null
);
INSERT INTO interview.student (id, name, age) VALUES (1001, '张三', 18);
INSERT INTO interview.student (id, name, age) VALUES (1002, '张四', 19);
INSERT INTO interview.student (id, name, age) VALUES (1003, '张五', 20);
INSERT INTO interview.student (id, name, age) VALUES (1004, '张六', 19);

-- 查询所有学生的数学成绩，显示学生姓名 name, 分数， 由高到低
SELECT a.name, b.score
FROM student a
LEFT JOIN grade b
ON a.id = b.id AND b.kemu='数学'
ORDER BY b.score DESC;

select a.name, b.score
from student a, grade b
where a.id=b.id and b.kemu='数学'
order by b.score desc;

-- 统计每个学生的总成绩,显示字段：姓名，总成绩
select a.name, sum(b.score) as sum_score
from student a, grade b
where a.id=b.id
group by name desc;

-- 统计每个学生的总成绩（由于学生可能有重复名字） ,显示字段：学生 id，姓名，总成绩
select a.id, a.name, c.sum_score
from student a,
     (select b.id, sum(b.score) sum_score
      from grade b
      group by id) c
where a.id = c.id
order by sum_score desc;

-- 列出各门课程成绩最好的学生， 要求显示字段: 学号，姓名,科目，成绩第一步先 group by 找出单科最好成绩，作为第一张表
select c.id, a.name, c.kemu, c.score
from grade c, student a,
(select b.kemu, max(b.score) max_score
from grade b
group by kemu) t
where c.kemu=t.kemu
and c.score=t.max_score
and a.id=c.id;

-- 列出各门课程成绩最好的 2 位学生， 要求显示字段: 学号，姓名, 科目，成绩
SELECT t1.id, a.name, t1.kemu, t1.score
FROM grade t1,
     student a
WHERE (SELECT count(*)
       FROM grade t2
       WHERE t1.kemu = t2.kemu
         AND t2.score > t1.score
      ) < 2
  and a.id = t1.id
ORDER BY t1.kemu, t1.score DESC;

-- 计算每个人的平均成绩， 要求显示字段: 学号，姓名，平均成绩
select a.id, a.name, c.avg_score
from student a,
     (select b.id, avg(b.score) as avg_score
         from grade b
         group by b.id) c
where a.id=c.id;

-- 计算每个人的成绩，总分数，平均分，要求显示：学号，姓名，语文，数学，英语，总分，平均分
SELECT a.id as 学号, a.name as 姓名,
sum(case when b.kemu='语文' then b.score else 0 end) as 语文,
sum(case when b.kemu='数学' then b.score else 0 end) as 数学,
sum(case when b.kemu='英语' then b.score else 0 end) as 英语,
sum(b.score) as 总分 ,
sum(b.score)/count(b.score) as 平均分
FROM student a, grade b
where a.id = b.id
GROUP BY b.id;

-- 列出各门课程的平均成绩，要求显示字段：课程，平均成绩
select b.kemu, avg(b.score)
from grade b
group by b.kemu;

-- 列出数学成绩的排名， 要求显示字段：学号，姓名，成绩，排名
SELECT t.id,
       a.name,
       t.score                  as 数学分数,
       @paiming := @paiming + 1 as 排名
FROM (SELECT b.id, b.score
      FROM grade b
      WHERE b.kemu = '数学') AS t,
     (SELECT @paiming := 0) r,
     student a
WHERE a.id = t.id
ORDER BY t.score DESC;

-- 列出数学成绩的排名， 要求显示字段：学号，姓名，成绩，排名，同一分数名次一样
SELECT t.id,
       a.name,
       t.score  as '数学分数',
       (CASE
            WHEN @temp = t.score THEN
                @paiming
            WHEN @temp := t.score THEN
                @paiming := @paiming + 1
            WHEN @temp = 0 THEN
                @paiming := @paiming + 1
           END) AS num
FROM (SELECT b.id, b.score
      FROM grade b
      WHERE b.kemu = '数学') AS t,
     (SELECT @paiming := 0, @temp := 0) r,
     student a
WHERE a.id = t.id
ORDER BY t.score DESC;

-- 列出数学成绩的排名， 要求显示字段：学号，成绩，排名，排名相同的占个名次
SELECT obj.id,
       obj.score              as '数学',
       @rownum := @rownum + 1 AS num_tmp,
       @incrnum := (CASE
                        WHEN @rowtotal = obj.score THEN
                            @incrnum
                        WHEN @rowtotal := obj.score THEN
                            @rownum
           END)               AS '排名'
FROM (SELECT id, score
      FROM grade
      WHERE kemu = '数学'
      ORDER BY score DESC
     ) AS obj,
     (SELECT @rownum := 0, @rowtotal := NULL, @incrnum := 0) r;

-- 列出数学成绩前 3 名的学生（要求显示字段：学号，姓名, 科目，成绩）
select a.id, a.name, b.kemu, b.score
from student a,
     grade b
where a.id = b.id
  and kemu = '数学'
order by score desc
limit 3;

-- 查询数学成绩第 2 和第 3 名的学生
select a.id, a.name, b.kemu, b.score
from student a,
     grade b
where a.id = b.id
  and kemu = '数学'
order by score desc
limit 1, 2;

-- 查询第 3 名到后面所有的学生数学成绩，使用一个非常大的数字
select a.id, a.name, b.kemu, b.score
from student a,
     grade b
where a.id = b.id
  and kemu = '数学'
order by score desc
limit 3, 10000;

-- 统计英语课程少于 80 分的，显示 学号 id, 姓名，科目，分数
select a.id, a.name, b.kemu, b.score
from student a,
     grade b
where a.id = b.id
  and b.kemu = '英语'
  and b.score < 80;

-- 统计每门课程不及格、一般、优秀的数量
SELECT b.kemu,
       (SELECT COUNT(*) FROM grade WHERE score < 60 and kemu = b.kemu) as `不及格`,
       (SELECT COUNT(*) FROM grade WHERE score between 60 and 80 and kemu = b.kemu) as `一般`,
       (SELECT COUNT(*) FROM grade WHERE score > 80 and kemu = b.kemu) as `优秀`
FROM grade b
GROUP BY kemu;

-- 查找每科成绩前 2 名，显示 id, 姓名，科目，分数
SELECT t1.id, a.name, t1.kemu, t1.score
FROM grade t1,
     student a
WHERE (SELECT count(*)
       FROM grade t2
       WHERE t1.kemu = t2.kemu
         AND t2.score >= t1.score
      ) <= 2
  and a.id = t1.id
ORDER BY t1.kemu, t1.score DESC;

-- 如果第二名有重复的，也能一起查找出来
SELECT t1.id, a.name, t1.kemu, t1.score
FROM grade t1,
     student a
WHERE (SELECT count(*)
       FROM grade t2
       WHERE t1.kemu = t2.kemu
         AND t2.score > t1.score
      ) < 2
  and a.id = t1.id
ORDER BY t1.kemu, t1.score DESC;

create table xuesheng
(
    name    varchar(20) null,
    kecheng varchar(20) null,
    score   int         null
);
insert into xuesheng values
('张三', '语文', 81),
('张三', '数学', 73),
('李四', '语文', 86),
('李四', '数学', 90),
('王五', '数学', 89),
('王五', '语文', 88),
('王五', '英语', 96);

-- 用一条 SQL 语句查询 xuesheng 表每门课都大于 80 分的学生姓名
SELECT name
FROM xuesheng
GROUP BY name
HAVING MIN(score) > 80;

SELECT DISTINCT name
FROM xuesheng
WHERE name NOT IN
(SELECT DISTINCT name
FROM xuesheng
WHERE score <=80);

-- 考虑课程大于3
SELECT name
FROM xuesheng
GROUP BY name
HAVING MIN(score)> 80
AND COUNT(kecheng)>=3;

-- 用 sql 查询出“张” 姓学生中平均成绩大于 75 分的学生信息
select *
from xuesheng
where name in
      (select name
       from xuesheng
       where name like '张%'
       group by name
       having avg(score) > 75);

-- 找出姓张和姓李的同学, 用 rlike 实现匹配多个
select *
from xuesheng
where name in
      (select name
       from xuesheng
       where name rlike '[张李]'
       group by name
       having avg(score) > 75);
