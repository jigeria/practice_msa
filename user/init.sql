create table USER_ACOOUNT (user_id SERIAL PRIMARY KEY, user_name VARCHAR(50) UNIQUE NOT NULL, phone_number VARCHAR(50) NOT NULL);
insert into USER_ACOOUNT VALUES (1,'sangmin','010-2222-3333');
insert into USER_ACOOUNT VALUES (2,'park','010-2642-4292');
insert into USER_ACOOUNT VALUES (3,'jigeria','010-8599-4292');
commit;
