# 1 create table
# in Linux terminal example
sqlite> create table students (
...> id integer primary key autoincrement, 
...> name varchar(20),
...> subj varchar(20),
...>  mark real);
sqlite .tables

sqlite> select * from students;  # >> empty table

sqlite> insert into students (name, subj, mark) values ('Bill', 'Math', 3);

sqlite> select * from students; #  1|Bill|Math|3.0

sqlite> insert into students (name, subj, mark) values ('Bill', 'DB', 3);
sqlite> insert into students (name, subj, mark) values ('Bill', 'Phys', 3);
sqlite> insert into students (name, subj, mark) values ('Bob', 'Math', 4);
sqlite> insert into students (name, subj, mark) values ('Bob', 'DB', 5);
sqlite> insert into students (name, subj, mark) values ('Bob', 'Phys', 3);
sqlite> insert into students (name, subj, mark) values ('Bill', 'Math', 2);

sqlite> select * from students; #  1|Bill|Math|3.0

sqlite> update students set mark=5 where mane='Bill' and subj='Math'; 
sqlite> select * from students;

sqlite> update students set mark=4 where id=7;
sqlite> select * from students;

sqlite> delete from students where id=7; # del all: sqlite> delete from students;

#SELECT:
sqlite> select name, subj from students;
sqlite> select 2 from students;# select for ev. line
sqlite> select id*mark from students;
sqlite> select distinct 'Name', name from students;
sqlite> select name, mark from students where mark>3;
sqlite> select distinct name from students where mark>3;
#select from select:
sqlite> select distinct name from (select name, mark from students where mark>3);
sqlite> select name, mark from students order by mark;
sqlite> select name, mark from students order by mark, name;
sqlite> select max(mark) from students;
sqlite> select avg(mark) from students;
sqlite> select name, avg(mark) from students group by name;
sqlite> select subj,  avg(mark) from students group by subj;

sqlite> select subj,  avg(mark) from students group by subj having avg(mark)>3;

sqlite> select * from students;

sqlite> create table groups(
...> st_name varchar(20), 
...> g_name varchar(20));
sqlite>  inert into groups values ('Bob', 'AA-11');
sqlite>  inert into groups values ('Bill', 'AA-12');
sqlite>  inert into groups values ('John', 'AA-11');
sqlite> select * from students, groups where students.name=st_name;
sqlite> select name, avg(mark), g_name from students, groups where students.name=st_name;