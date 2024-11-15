select productName, sum(quantityordered * priceeach) as totalSales from orderdetails natural join products group by productname order by totalSales desc limit 5;
