create table students (
  student_id serial primary key,
  first_name varchar(50) not null,
  last_name varchar(50) not null,
  homeroom_num smallint,
  phone varchar(25) not null unique,
  email varchar(100) not null unique,
  grad_year smallint
);