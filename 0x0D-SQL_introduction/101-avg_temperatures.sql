-- import in hbtn_0c_0 database this table dump: temperatures.sql 
-- code for import -> mysql -uroot -p hbtn_0c_0  < temperatures.sql

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
