create view q5 as select orderNumber, orderDate, shippedDate, customerName, salesRepEmployeeNumber from customers natural join orders where shippeddate is not null;
