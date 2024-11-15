select customerName, c.postalCode, c.city from customers c join offices o on c.postalCode=o.postalCode;
