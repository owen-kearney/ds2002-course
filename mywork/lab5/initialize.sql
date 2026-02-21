use ratfeeder;
create table cookies (cookieid integer primary key auto_increment, type_of_cookie text, diameter integer);
create table rats (ratid integer primary key auto_increment, rat_name text, rat_weight integer, cookieid integer);

insert into cookies (type_of_cookie, diameter) values ('chocolate chip', 5);
insert into cookies (type_of_cookie, diameter) values ('sugar', 4);
insert into cookies (type_of_cookie, diameter) values ('peanut butter', 6);
insert into cookies (type_of_cookie, diameter) values ('chocolate chip', 11);
insert into cookies (type_of_cookie, diameter) values ('oatmeal raisin', 5);
insert into cookies (type_of_cookie, diameter) values ('macaroon', 3);
insert into cookies (type_of_cookie, diameter) values ('gingerbread', 7);
insert into cookies (type_of_cookie, diameter) values ('shortbread', 6);
insert into cookies (type_of_cookie, diameter) values ('snickerdoodle', 5);
insert into cookies (type_of_cookie, diameter) values ('butter', 8);
insert into cookies (type_of_cookie, diameter) values ('chocolate chip', 20);

insert into rats (rat_name, rat_weight, cookieid) values ('Frederick', 150, 3);
insert into rats (rat_name, rat_weight, cookieid) values ('Mohammad', 125, 9);
insert into rats (rat_name, rat_weight, cookieid) values ('Anya', 200, 7);
insert into rats (rat_name, rat_weight, cookieid) values ('Rachaad', 168, 10);
insert into rats (rat_name, rat_weight, cookieid) values ('Armando', 400, 4);
insert into rats (rat_name, rat_weight, cookieid) values ('Tabitha', 110, 1);
insert into rats (rat_name, rat_weight, cookieid) values ('Bea', 147, 5);
insert into rats (rat_name, rat_weight, cookieid) values ('Melissa', 165, 2);
insert into rats (rat_name, rat_weight, cookieid) values ('Richard', 185, 8);
insert into rats (rat_name, rat_weight, cookieid) values ('Ratty McCheesepants Esq.', 670, 6);
insert into rats (rat_name, rat_weight, cookieid) values ('Elaina', 150, 11);