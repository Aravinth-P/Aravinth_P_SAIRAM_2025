CREATE TABLE Employees(
	   EmployeeID int,
     FirstName varchar(100),
     LastName varchar(100),
     Email varchar(100),
     Department varchar(100),
     Salary int
);
CREATE TABLE Customers(
	   CustomerID int,
     FirstName varchar(100),
     LastName varchar(100),
     Email varchar(100),
     Phonenumber bigint,
     Address varchar(100)
);
CREATE TABLE Products(
	   ProductID int,
     ProductName varchar(100),
     Description varchar(100),
     Price int,
     QuantityinStock int
);
CREATE TABLE Books(
	   BookID int,
     Title varchar(100),
     Author varchar(100),
     PublicationYear year
);
CREATE TABLE Events(
	   EventID int,
     EventName varchar(100),
     Date date,
     StartTime time,
     Location varchar(100),
     Organizer varchar(100)     
);
CREATE TABLE Orders(
	   OrderID int,
     CustomerID int,
     OrderDate date,
     TotalAmount int,
     Status varchar(100)
);
