select customerName from customers natural join orders natural join orderdetails natural join products group by customername having count(distinct productline) >= 0.25 * (select count(*) from productlines);
