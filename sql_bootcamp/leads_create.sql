create table leads (
  cust_id serial primary key,
  fname varchar(50) not null,
  lname varchar(50) not null,
  email varchar(300) unique not null,
  dwell_time smallint
);