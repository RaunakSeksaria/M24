select productName from products group by productname having count(distinct productvendor) > 1;
