```
-- TRIGGER
CREATE TRIGGER orders_bu
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
 INSERT INTO dont_sell(customerName, `SUM(amount)`)
 VALUES("sanaz", 1203);
END
```

```
START TRANSACTION;

UPDATE dont_sell 

SET customerName="dddd"
where customerName='Porto Imports Co.';

INSERT INTO dont_sell(customerName, `SUM(amount)`)
 VALUES("sanaz", 1203);
 
COMMIT
```

```
CREATE PROCEDURE test_pro_2(IN a INTEGER, OUT b VARCHAR(50))
BEGIN
  SELECT * from orders WHERE orders.number_year>a;
END

DROP PROCEDURE test_pro_2

SET @a;
CALL test_pro_2(18, @a)
```
```
CREATE view view2 as 
SELECT * from orders 

SELECT * FROM view2
```

```
SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM locations AS l
LEFT JOIN countries AS c
on l.country_id = c.country_id
```

```
CREATE TRIGGER triger_phone2
BEFORE INSERT
ON employees FOR EACH ROW
BEGIN


   IF new.phone LIKE 'ddd-ddd-ddd' THEN
      SET new.last_name = 'correct';
   ELSE
      SET new.last_name = 'wrong!!';

   END IF;

END; 
```

```
CREATE TRIGGER triger_phone
BEFORE INSERT
ON employees FOR EACH ROW
BEGIN
   IF  new.phone LIKE 'ddd-ddd-ddd' THEN
		INSERT into employees set phone = new.phone;
   ELSE
       INSERT into employees set phone = 'error';
   END IF;
END; 
```

```
INSERT INTO employees
(phone) VALUES('913-292-123');
```

```
SHOW TRIGGERS
DROP TRIGGER triger_phone
```

```
CREATE TABLE tbl
(id int AUTO_INCREMENT PRIMARY KEY
, `name` VARCHAR) 
AUTO_INCREMENT = 100;
```

```
CREATE TABLE tbl (
    id int ,
    FirstName varchar(255),
    PRIMARY KEY (id)

);
```

```
ALTER TABLE tbl AUTO_INCREMENT = 10;
```

```
INSERT INTO tbl
(FirstName) VALUES('sara');
```

```
SELECT e.first_name, e.last_name, d.department_id, d.depatment_name
FROM employees e
LEFT JOIN departments d
on e.DEPARTMENT_ID = d.department_id 
```


```
-- Write a query to find the name (first_name, last_name), job, department ID and name of the employees who works in London
SELECT e.first_name, e.last_name, d.depatment_name, d.department_id, d.location_id -- , l.city
FROM employees AS e
LEFT JOIN departments as d
on e.DEPARTMENT_ID = d.department_id
LEFT JOIN locations as l
on d.location_id=l.location_id -- ?????????????????????????????????????
where l.city='Liverpool'
```

```
-- #4. Write a query to find the employee id, name (last_name) along with their manager_id and name (last_name)
SELECT e.first_name, e.last_name, e.DEPARTMENT_ID, e.manager_id
FROM employees AS e
```

```
-- Write a query to find the name (first_name, last_name) and hire date of the employees who was hired after 'Jones'.

SELECT e.first_name, e.last_name, e.hire_date
FROM employees AS e
WHERE DATE_FORMAT(e.hire_date, "%m") >6
```

```
-- Write a query to get the department name and number of employees in the department.
SELECT COUNT(d.depatment_name), d.depatment_name
FROM employees as e
LEFT JOIN departments as d
on d.department_id = e.DEPARTMENT_ID
GROUP BY d.department_id
```

```
-- 222222222

SELECT COUNT(*), d.depatment_name
FROM departments as d
LEFT JOIN employees as e
on d.department_id = e.DEPARTMENT_ID
WHERE e.EMPLOYEE_ID is NOT NULL
GROUP BY d.department_id
```

```
-- 3333333333
SELECT COUNT(*), d.depatment_name
FROM departments as d
INNER JOIN employees as e
on d.department_id = e.DEPARTMENT_ID
GROUP BY d.department_id
```

```
--  Write a query to display the department ID and name and first name of manager
SELECT e.first_name, e.last_name
FROM employees as e
LEFT JOIN departments as d
on e.DEPARTMENT_ID = d.department_id
```

```
-- Write a query to display the job title and average salary of employees. Go to the editor
SELECT AVG(e.salary)
FROM employees as e
GROUP BY e.job_id
```

```
-- Write a query to display job title, employee name, and the difference between salary of the employee and minimum salary for the job.
SELECT salary - m
FROM employees
SET m = (SELECT MIN(e.salary)
             FROM employees as e
              GROUP BY e.job_id)

set GLOBAL f = SELECT MIN(e.salary)
             FROM employees as e
```
							
```							
SELECT salary- f
FROM employees
```

```
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'STRICT_TRANS_TABLES',''));
```

```
SHOW VARIABLES LIKE 'sql_mode';
```

```
SELECT sql_mode
```

```
SET SESSION sql_mode = sys.list_add(@@session.sql_mode, 'ONLY_FULL_GROUP_BY');
```


```
-- --------------            it is greaaaaaat
SELECT e.salary- e_m_j.m, e.job_id, e.first_name, e_m_j.m
FROM employees e
LEFT JOIN 	(SELECT MIN(salary) as m, job_id
							FROM employees
							GROUP BY job_id) as e_m_j
on e_m_j.job_id = e.job_id

--               ==========================================
```

```
ALTER TABLE employees 
ADD COLUMN interesting ENUM('low','med','high')

INSERT INTO  employees(interesting) SELECT interesting FROM employees  WHERE manager_id=200


DELETE FROM employees WHERE DEPARTMENT_ID is NULL
```

```

update employees                                -- ----------------------------- have an another way?
SET interesting = CASE salary
												WHEN 50 THEN 'low'
												WHEN 200 THEN 'med'
												WHen 100 THEN 'high'
												ELSE 'low'
											END;
where interesting is null;
```

-- ====================================================================
```
SHOW INDEX FROM employees
```

```
EXPLAIN SELECT * FROM employees WHERE DEPARTMENT_ID=10 


CREATE INDEX test_time on employees(DEPARTMENT_ID)


SELECT * FROM employees WHERE DEPARTMENT_ID=12


SET profiling = 1;
```


```
show PROFILEs
```

```
SELECT * from employees e LEFT JOIN employees e2 on e.salary < e2.salary 
```

```
SELECT * 
FROM (SELECT max(salary) as sm  FROM employees) as test_v
LEFT JOIN  employees as e
on e.salary =  test_v.sm
```

```
SELECT *
FROM employees e
LEFT JOIN employees e2 ON e.salary < e2.salary
where e2.salary is null
```

```
SELECT salary FROM employees
UNION
SELECT salary FROM employees
ORDER BY salary;
```

```
-- ================================== it s beautiful
select e.salary - n.salary
FROM employees e
LEFT JOIN employees e2 ON e.salary < e2.salary
CROSS JOIN employees n
WHERE e2.salary is null
```





