create table USER_ACOOUNT (user_id SERIAL PRIMARY KEY, user_name VARCHAR(50) UNIQUE NOT NULL, phone_number VARCHAR(50) NOT NULL);
insert into USER_ACOOUNT VALUES (1,'sangmin','1234-5678-5592-2323');
insert into USER_ACOOUNT VALUES (2,'park','1234-5678-5592-2323');
insert into USER_ACOOUNT VALUES (3,'jigeria','1234-5678-5592-2323');
commit;
