select employeeNumber, firstName, lastName from employees e where not exists (select * from employees where reportsto=e.employeenumber);
