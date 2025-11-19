SELECT * FROM series;
select * from series where has_won_awards;
select * from series where rating > 2.5;
select * from series where country = 'NL' and language = 'NL';
select * from series where seasons < 5;
select * from series where seasons < 3 or seasons > 20;
select * from series where title like '%th%';
select * from series where not seasons = 3;

select * from series where rating > 2.5 order by rating desc;
select title, seasons FROM series where seasons < 5 order by seasons asc;
select title, seasons, country from series where seasons < 3 or seasons > 20 order by seasons asc, country asc;