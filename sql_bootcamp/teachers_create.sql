create table teachers (
  teacher_id serial primary key,
  first_name varchar(50) not null unique,
  last_name varchar(50) not null unique,
  homeroom_num smallint,
  department varchar(100),
  email varchar(100) not null unique,
  phone varchar(25) not null unique
);