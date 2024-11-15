select customerName from customers where customernumber not in (select customernumber from orders);
