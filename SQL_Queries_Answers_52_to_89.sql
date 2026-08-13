
================================================================================
                    SQL QUERIES - ANSWERS (Questions 52-89)
                    JALA Academy Assignment
================================================================================

TABLES:
-------
SALESPEOPLE (SNUM, SNAME, CITY, COMM)
CUST      (CNUM, CNAME, CITY, RATING, SNUM)
ORDERS    (ONUM, AMT, ODATE, CNUM, SNUM)

================================================================================
Q52. Obtain all orders for the customer named Cisnerous.
     (Assume you don't know his customer no. (cnum))
================================================================================

SELECT o.*
FROM orders o
WHERE o.cnum = (SELECT cnum FROM cust WHERE cname = 'Cisnerous');

-- OR using JOIN:
SELECT o.*
FROM orders o
JOIN cust c ON o.cnum = c.cnum
WHERE c.cname = 'Cisnerous';

================================================================================
Q53. Produce the names and rating of all customers who have above average orders.
================================================================================

SELECT DISTINCT c.cname, c.rating
FROM cust c
JOIN orders o ON c.cnum = o.cnum
WHERE o.amt > (SELECT AVG(amt) FROM orders);

================================================================================
Q54. Find total amount in orders for each salesperson for whom this total
     is greater than the amount of the largest order in the table.
================================================================================

SELECT snum, SUM(amt) AS total_amount
FROM orders
GROUP BY snum
HAVING SUM(amt) > (SELECT MAX(amt) FROM orders);

================================================================================
Q55. Find all customers with order on 3rd Oct.
================================================================================

SELECT DISTINCT c.*
FROM cust c
JOIN orders o ON c.cnum = o.cnum
WHERE o.odate = '03-OCT-94';

-- OR:
SELECT * FROM cust
WHERE cnum IN (SELECT cnum FROM orders WHERE odate = '03-OCT-94');

================================================================================
Q56. Find names and numbers of all salesperson who have more than one customer.
================================================================================

SELECT s.snum, s.sname
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname
HAVING COUNT(c.cnum) > 1;

================================================================================
Q57. Check if the correct salesperson was credited with each sale.
================================================================================

SELECT o.onum, o.snum AS order_snum, c.snum AS cust_snum,
       CASE WHEN o.snum = c.snum THEN 'Correct' ELSE 'Incorrect' END AS status
FROM orders o
JOIN cust c ON o.cnum = c.cnum;

================================================================================
Q58. Find all orders with above average amounts for their customers.
================================================================================

SELECT o.*
FROM orders o
WHERE o.amt > (SELECT AVG(amt) FROM orders o2 WHERE o2.cnum = o.cnum);

-- OR using JOIN:
SELECT o.*
FROM orders o
JOIN (SELECT cnum, AVG(amt) AS avg_amt FROM orders GROUP BY cnum) avg_tbl
     ON o.cnum = avg_tbl.cnum
WHERE o.amt > avg_tbl.avg_amt;

================================================================================
Q59. Find the sums of the amounts from order table grouped by date,
     eliminating all those dates where the sum was not at least 2000
     above the maximum amount.
================================================================================

SELECT odate, SUM(amt) AS total_amt
FROM orders
GROUP BY odate
HAVING SUM(amt) >= (SELECT MAX(amt) + 2000 FROM orders);

================================================================================
Q60. Find names and numbers of all customers with ratings equal to the
     maximum for their city.
================================================================================

SELECT c.cnum, c.cname, c.city, c.rating
FROM cust c
WHERE c.rating = (SELECT MAX(rating) FROM cust c2 WHERE c2.city = c.city);

================================================================================
Q61. Find all salespeople who have customers in their cities who they
     don't service. (Both way using Join and Correlated subquery.)
================================================================================

-- Using JOIN:
SELECT DISTINCT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.city = c.city
WHERE s.snum != c.snum;

-- Using Correlated Subquery:
SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE EXISTS (
    SELECT 1 FROM cust c
    WHERE c.city = s.city AND c.snum != s.snum
);

================================================================================
Q62. Extract cnum, cname and city from customer table if and only if
     one or more of the customers in the table are located in San Jose.
================================================================================

SELECT cnum, cname, city
FROM cust
WHERE EXISTS (SELECT 1 FROM cust c2 WHERE c2.city = 'San Jose');

================================================================================
Q63. Find salespeople no. who have multiple customers.
================================================================================

SELECT snum
FROM cust
GROUP BY snum
HAVING COUNT(cnum) > 1;

================================================================================
Q64. Find salespeople number, name and city who have multiple customers.
================================================================================

SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE s.snum IN (
    SELECT snum FROM cust GROUP BY snum HAVING COUNT(cnum) > 1
);

-- OR using JOIN:
SELECT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname, s.city
HAVING COUNT(c.cnum) > 1;

================================================================================
Q65. Find salespeople who serve only one customer.
================================================================================

SELECT s.snum, s.sname
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname
HAVING COUNT(c.cnum) = 1;

-- OR:
SELECT snum FROM cust
GROUP BY snum
HAVING COUNT(cnum) = 1;

================================================================================
Q66. Extract rows of all salespeople with more than one current order.
================================================================================

SELECT s.*
FROM salespeople s
WHERE s.snum IN (
    SELECT snum FROM orders GROUP BY snum HAVING COUNT(onum) > 1
);

-- OR using JOIN:
SELECT DISTINCT s.*
FROM salespeople s
JOIN orders o ON s.snum = o.snum
GROUP BY s.snum, s.sname, s.city, s.comm
HAVING COUNT(o.onum) > 1;

================================================================================
Q67. Find all salespeople who have customers with a rating of 300.
     (use EXISTS)
================================================================================

SELECT s.snum, s.sname
FROM salespeople s
WHERE EXISTS (
    SELECT 1 FROM cust c
    WHERE c.snum = s.snum AND c.rating = 300
);

================================================================================
Q68. Find all salespeople who have customers with a rating of 300.
     (use Join)
================================================================================

SELECT DISTINCT s.snum, s.sname
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE c.rating = 300;

================================================================================
Q69. Select all salespeople with customers located in their cities
     who are not assigned to them. (use EXISTS)
================================================================================

SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE EXISTS (
    SELECT 1 FROM cust c
    WHERE c.city = s.city AND c.snum != s.snum
);

================================================================================
Q70. Extract from customers table every customer assigned to a salesperson
     who currently has at least one other customer (besides the customer
     being selected) with orders in order table.
================================================================================

SELECT c.*
FROM cust c
WHERE c.snum IN (
    SELECT snum FROM cust
    GROUP BY snum
    HAVING COUNT(cnum) > 1
)
AND c.cnum IN (SELECT cnum FROM orders);

================================================================================
Q71. Find salespeople with customers located in their cities
     (using both ANY and IN)
================================================================================

-- Using IN:
SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE s.city IN (SELECT city FROM cust WHERE cust.snum = s.snum);

-- Using ANY:
SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE s.city = ANY (SELECT city FROM cust WHERE cust.snum = s.snum);

================================================================================
Q72. Find all salespeople for whom there are customers that follow them
     in alphabetical order. (Using ANY and EXISTS)
================================================================================

-- Using EXISTS:
SELECT s.snum, s.sname
FROM salespeople s
WHERE EXISTS (
    SELECT 1 FROM cust c
    WHERE c.snum = s.snum AND c.cname > s.sname
);

-- Using ANY:
SELECT s.snum, s.sname
FROM salespeople s
WHERE s.sname < ANY (
    SELECT c.cname FROM cust c WHERE c.snum = s.snum
);

================================================================================
Q73. Select customers who have a greater rating than any customer in Rome.
================================================================================

SELECT * FROM cust
WHERE rating > ANY (SELECT rating FROM cust WHERE city = 'Rome');

-- OR:
SELECT * FROM cust
WHERE rating > (SELECT MIN(rating) FROM cust WHERE city = 'Rome');

================================================================================
Q74. Select all orders that had amounts that were greater than at least
     one of the orders from Oct 6th.
================================================================================

SELECT * FROM orders
WHERE amt > ANY (SELECT amt FROM orders WHERE odate = '06-OCT-94');

-- OR:
SELECT * FROM orders
WHERE amt > (SELECT MIN(amt) FROM orders WHERE odate = '06-OCT-94');

================================================================================
Q75. Find all orders with amounts smaller than any amount for a customer
     in San Jose. (Both using ANY and without ANY)
================================================================================

-- Using ANY:
SELECT * FROM orders
WHERE amt < ANY (SELECT amt FROM orders o2
                 JOIN cust c ON o2.cnum = c.cnum
                 WHERE c.city = 'San Jose');

-- Without ANY (using MIN):
SELECT * FROM orders
WHERE amt < (SELECT MIN(amt) FROM orders o2
             JOIN cust c ON o2.cnum = c.cnum
             WHERE c.city = 'San Jose');

================================================================================
Q76. Select those customers whose ratings are higher than every customer
     in Paris. (Using both ALL and NOT EXISTS)
================================================================================

-- Using ALL:
SELECT * FROM cust
WHERE rating > ALL (SELECT rating FROM cust WHERE city = 'Paris');

-- Using NOT EXISTS:
SELECT c1.* FROM cust c1
WHERE NOT EXISTS (
    SELECT 1 FROM cust c2
    WHERE c2.city = 'Paris' AND c2.rating >= c1.rating
);

================================================================================
Q77. Select all customers whose ratings are equal to or greater than
     ANY of the Serres.
================================================================================

SELECT * FROM cust
WHERE rating >= ANY (SELECT rating FROM cust c2
                     JOIN salespeople s ON c2.snum = s.snum
                     WHERE s.sname = 'Serres');

================================================================================
Q78. Find all salespeople who have no customers located in their city.
     (Both using ANY and ALL)
================================================================================

-- Using ALL:
SELECT s.* FROM salespeople s
WHERE s.city != ALL (SELECT city FROM cust WHERE city IS NOT NULL);

-- Using NOT EXISTS (alternative):
SELECT s.* FROM salespeople s
WHERE NOT EXISTS (
    SELECT 1 FROM cust c WHERE c.city = s.city
);

================================================================================
Q79. Find all orders for amounts greater than any for the customers in London.
================================================================================

SELECT * FROM orders
WHERE amt > ANY (SELECT amt FROM orders o2
                 JOIN cust c ON o2.cnum = c.cnum
                 WHERE c.city = 'London');

================================================================================
Q80. Find all salespeople and customers located in London.
================================================================================

SELECT snum, sname, city, 'Salesperson' AS type
FROM salespeople
WHERE city = 'London'
UNION
SELECT cnum, cname, city, 'Customer' AS type
FROM cust
WHERE city = 'London';

================================================================================
Q81. For every salesperson, dates on which highest and lowest orders were brought.
================================================================================

SELECT snum,
       odate,
       MAX(amt) AS highest_order,
       MIN(amt) AS lowest_order
FROM orders
GROUP BY snum, odate;

================================================================================
Q82. List all of the salespeople and indicate those who don't have customers
     in their cities as well as those who do have.
================================================================================

SELECT s.snum, s.sname, s.city,
       CASE WHEN c.cnum IS NOT NULL THEN 'Has customers in city'
            ELSE 'No customers in city' END AS status
FROM salespeople s
LEFT JOIN cust c ON s.city = c.city AND s.snum = c.snum;

================================================================================
Q83. Append strings to the selected fields, indicating whether or not a
     given salesperson was matched to a customer in his city.
================================================================================

SELECT s.snum, s.sname, s.city,
       CASE WHEN EXISTS (
           SELECT 1 FROM cust c WHERE c.city = s.city AND c.snum = s.snum
       ) THEN s.sname || ' - Matched in city'
       ELSE s.sname || ' - Not matched in city' END AS status
FROM salespeople s;

-- For SQL Server:
SELECT s.snum, s.sname, s.city,
       CASE WHEN EXISTS (
           SELECT 1 FROM cust c WHERE c.city = s.city AND c.snum = s.snum
       ) THEN CONCAT(s.sname, ' - Matched in city')
       ELSE CONCAT(s.sname, ' - Not matched in city') END AS status
FROM salespeople s;

================================================================================
Q84. Create a union of two queries that shows the names, cities and ratings
     of all customers. Those with a rating of 200 or greater will also have
     the words 'High Rating', while the others will have the words 'Low Rating'.
================================================================================

SELECT cname, city, rating, 'High Rating' AS rating_category
FROM cust
WHERE rating >= 200
UNION
SELECT cname, city, rating, 'Low Rating' AS rating_category
FROM cust
WHERE rating < 200;

================================================================================
Q85. Write command that produces the name and number of each salesperson
     and each customer with more than one current order. Put the result in
     alphabetical order.
================================================================================

SELECT s.snum AS id, s.sname AS name, 'Salesperson' AS role
FROM salespeople s
WHERE s.snum IN (
    SELECT snum FROM orders GROUP BY snum HAVING COUNT(onum) > 1
)
UNION
SELECT c.cnum AS id, c.cname AS name, 'Customer' AS role
FROM cust c
WHERE c.cnum IN (
    SELECT cnum FROM orders GROUP BY cnum HAVING COUNT(onum) > 1
)
ORDER BY name;

================================================================================
Q86. Form a union of three queries. Have the first select the snums of all
     salespeople in San Jose, then second the cnums of all customers in San Jose
     and the third the onums of all orders on Oct. 3. Retain duplicates between
     the last two queries, but eliminates redundancies between either of them
     and the first.
================================================================================

SELECT snum AS id FROM salespeople WHERE city = 'San Jose'
UNION
SELECT cnum AS id FROM cust WHERE city = 'San Jose'
UNION ALL
SELECT onum AS id FROM orders WHERE odate = '03-OCT-94';

================================================================================
Q87. Produce all the salesperson in London who had at least one customer there.
================================================================================

SELECT s.*
FROM salespeople s
WHERE s.city = 'London'
AND EXISTS (SELECT 1 FROM cust c WHERE c.city = 'London' AND c.snum = s.snum);

================================================================================
Q88. Produce all the salesperson in London who did not have customers there.
================================================================================

SELECT s.*
FROM salespeople s
WHERE s.city = 'London'
AND NOT EXISTS (SELECT 1 FROM cust c WHERE c.city = 'London' AND c.snum = s.snum);

================================================================================
Q89. We want to see salespeople matched to their customers without excluding
     those salesperson who were not currently assigned to any customers.
     (Use OUTER join and UNION)
================================================================================

-- Using LEFT OUTER JOIN:
SELECT s.snum, s.sname, c.cnum, c.cname
FROM salespeople s
LEFT JOIN cust c ON s.snum = c.snum;

-- Using UNION (to include unmatched from both sides):
SELECT s.snum, s.sname, c.cnum, c.cname
FROM salespeople s
LEFT JOIN cust c ON s.snum = c.snum
UNION
SELECT s.snum, s.sname, c.cnum, c.cname
FROM salespeople s
RIGHT JOIN cust c ON s.snum = c.snum;

================================================================================
                              END OF ANSWERS
================================================================================
