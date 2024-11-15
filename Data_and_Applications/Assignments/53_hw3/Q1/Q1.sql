select customerName, sum(quantityordered * priceeach) as totalOrderAmount from customers natural join orders natural join orderdetails group by customername;
