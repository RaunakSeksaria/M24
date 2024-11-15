delete from orderdetails where ordernumber in (select ordernumber from orders where orderstatus='Pending' and orderdate < curdate() - interval 1 month);
delete from orders where orderstatus='Pending' and orderdate < curdate() - interval 1 month;
