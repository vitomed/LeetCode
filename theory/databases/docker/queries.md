create table user
```postgres-sql
create table users (
    id serial primary key,
    uname varchar (50) unique not null,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);
```

insert user
```postgres-sql
INSERT INTO users (id, uname)
VALUES
    ('1', 'user1'),
    ('2', 'user2');
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
INSERT INTO books (id, user_id, count, fk_users)
VALUES
    (1, 1, 100, 1);
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