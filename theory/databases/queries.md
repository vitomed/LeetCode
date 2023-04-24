connect to db
```
psql -p 5432 -h localhost -d db -U user 
```

create table user
```postgres-sql
create table users (
    id serial primary key,
    uname varchar (50) unique not null,
);
```

insert user
```postgres-sql
insert into users (id, uname)
values
    ('3', 'user3');
```

```postgres-sql
insert into users
  select i, concat('user', i)
  from generate_series(4, 1000000) AS i;
```
drop column
```postgres-sql
alter table users
drop column created_on;
```

select
```postgres-sql
select * from users;
```
explain
```postgres-sql
explain select * from users;
explain select * from users where users.id='1';
explain select * from users where users.uname='user1';
```
create table book
```postgres-sql
create table books (
    id serial primary key,
    user_id int not null,
    count int NOT NULL,
    constraint fk_users FOREIGN KEY(user_id) REFERENCES users(id)
);
```
insert book
```postgres-sql
insert into books (id, user_id, count)
values
    (4, 2, 80);
```
select book
```postgres-sql
begin;
select count from books where books.id=1;
```
update book
```postgres-sql
begin;
update books set count=100-10 where books.id=1;
```
explain books
```postgres-sql
explain select count(*) from books where books.count > 100 and books.id > 1;
explain select * from users where users.id='1';
explain select * from users where users.uname='user1';
explain select * from users cross join books;
explain select * from users left join books on users.id = books.user_id;
explain select * from users right join books on users.id = books.user_id;
```
cross join
```postgres-sql
select * from users cross join books;
```
inner join
```postgres-sql
select * from users inner join books on users.id = books.user_id;
```
left join
```postgres-sql
select * from users left join books on users.id = books.user_id;
```
right join
```postgres-sql
select * from users right join books on users.id = books.user_id;
```
full join
```postgres-sql
select * from users full join books on users.id = books.user_id;
```

drop column
```postgres-sql
alter table users
drop column last_login;
```

drop constraint
```postgres-sql
alter table books
drop constraint fk_users;
```