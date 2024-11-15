select productName from products p where quantityinstock > (select avg(quantityinstock) from products where productline=p.productline);
