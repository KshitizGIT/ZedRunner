create table races (
city varchar(100),
class INT,
country_code varchar(10),
fee FLOAT,
length INT,
name VARCHAR(1000),
prizepool_first VARCHAR(1000),
prizepool_second VARCHAR(1000),
prizepool_third  VARCHAR(1000),
prizepool_total VARCHAR(1000),
race_id VARCHAR(20),
start_time VARCHAR(100),
status  VARCHAR(100),
weather VARCHAR(100),
PRIMARY KEY(race_id)
)
