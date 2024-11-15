select customerName, creditLimit, totalOrderAmount from (select customernumber, customername, creditlimit, sum(quantityordered * priceeach) as totalorderamount from customers natural join orders natural join orderdetails group by customernumber) as total where totalorderamount > 0.01 * creditlimit;
