CREATE TABLE test1234(
name VARCHAR(50),
family VARCHAR(50),
age INT
)

-- سطرهایی برگردند که با s شروع می شوند
SELECT * 
FROM employees
WHERE firstName LIKE 's%'

-- چتد شغل داریم 
SELECT COUNT(DISTINCT jobTitle) 
FROM employees

-- از هر کدام از شفل ها چند کارمند دارد
SELECT jobTitle, COUNT(jobTitle)
FROM employees
GROUP BY jobTitle
HAVING LIKE jobTitle 's%'

-- اضافه کردن ستون id به جدول قبل
ALTER TABLE test1234
ADD COLUMN id INT PRIMARY KEY

-- جدولی با کلید اصلی و کلید خارجی
CREATE TABLE test_fp(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
id_test1234 INT,
FOREIGN KEY(id_test1234) REFERENCES test1234(id) ON DELETE CASCADE
)

-- نام افرادی که هر کس باید به آن ریپورت تحویل دهد چیست؟
SELECT e1.firstName, e1.lastName, e1.reportsTo, 
       e2.firstName, e2.lastName, e1.employeeNumber
FROM employees AS e1 LEFT JOIN employees AS e2
ON e1.reportsTo = e2.employeeNumber

-- هر خریدار در مجموع چقدر خرید داشته است؟
DROP TABLE test3


DESCRIBE customers

DESCRIBE orders

DESCRIBE products

SELECT customerName, SUM(amount)
FROM customers AS c LEFT JOIN payments as p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber

-- مشتریانی که خرید نکرده اند را در یک جدول حدا اضافه کند.
CREATE TABLE dont_sell AS
SELECT customerName, SUM(amount)
FROM customers AS c LEFT JOIN payments as p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber
HAVING SUM(amount) IS NULL

-- اضافه کردن یک سطر به جدول
INSERT INTO test1234(id, name, family, age)
VALUES(2, 'ddd', 'ffff', 10)

-- 
SHOW DATABASES
SHOW TABLES

-- اگر میزان خرید از 60000 کمتر بود مقدار کم اگر بیشتر بود تا 100000 بود متوسط و اگر بیش از این بود زیاد دسته بندی شود یک ستون جدید.
SELECT customerName, SUM(amount) AS sum_amount, CASE 
	WHEN SUM(amount)>60000 THEN "medium"
	WHEN SUM(amount)<60000 THEN "small"
	ELSE "large" 
	END AS `status`
FROM customers AS c LEFT JOIN payments as p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber
HAVING SUM(amount) is not null

-- برای شمارش هر یک از این وضعیت ها:
SELECT `status`, COUNT(`status`)
from (
SELECT customerName, SUM(amount) AS sum_amount, CASE 
	WHEN SUM(amount)<60000 THEN "small"
	WHEN SUM(amount)<80000 and 60000<SUM(amount) THEN "medium"
	WHEN SUM(amount)>80000 THEN "large"
	END AS `status`
FROM customers AS c LEFT JOIN payments as p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber
HAVING SUM(amount) is not null)
as sub_query
GROUP BY `status`

-- union all UNION in 

SELECT employeeNumber
from employees
WHERE employeeNumber in (1002, 1003, 1012)
union
SELECT customerNumber
FROM customers

-- round
SELECT customerName, ROUND(avg(amount))
FROM customers AS c LEFT JOIN payments as p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber

-- exists
SELECT * 
FROM customers
WHERE EXISTS (SELECT * from employees WHERE customerNumber<employees.employeeNumber )

-- trigger
CREATE TRIGGER before_employees_update
BEFORE UPDATE ON employees 
FOR EACH ROW
begin
INSERT INTO test1234(id, name, family, age) VALUES(12, 'ddd','ssss',22);
END


UPDATE employees SET firstName='amirreza' WHERE email='sanaz'

-- view 
CREATE VIEW view1 AS
SELECT * FROM employees WHERE email='sanaz' or firstName='sanaz'

SELECT *
FROM view1

-- transaction

START TRANSACTION; 
SELECT * FROM employees;
SELECT * FROM customers;
INSERT INTO test1234(id, name, family, age) VALUES(12, 'ddd','ssss',22);
COMMIT


-- PROCEDURE
CREATE PROCEDURE test_pro(IN name varchar(50), OUT info VARCHAR(50))
BEGIN
SELECT email FROM employees WHERE firstName like name;
END

DROP PROCEDURE test_pro

SET @name=null;
call test_pro('l%',@name)


