create view q8 as select customerName, paymentDate, amount from customers natural join payments;
