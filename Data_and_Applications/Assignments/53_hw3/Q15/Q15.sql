select distinct customerName from customers natural join orders natural join payments where paymentdate > shippeddate and shippeddate is not null;
