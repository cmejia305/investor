create table cohort2
(
    user_id serial primary key,
    first_name text not null,
    last_name text not null,
    phone_number text not null
)
​
insert into cohort2(first_name, last_name, phone_number)
values('Julia', 'Otano', '7653332222'),
('Pedro', 'Otano', '7653332222'),
('Juan', 'Otano', '7653332222')
​
​
select * from cohort2 order by user_id asc
​
delete from cohort2 where user_id = 14
​
update cohort2 set first_name = 'Dunieski' where user_id = 8
​
select user_id, first_name from cohort2 where user_id = 8
​
​
​
CREATE SEQUENCE serial START 1
​
