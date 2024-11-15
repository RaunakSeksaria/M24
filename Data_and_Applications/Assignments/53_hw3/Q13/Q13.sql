select customerName, amount from customers natural join payments where amount > (select avg(amount) from payments);
