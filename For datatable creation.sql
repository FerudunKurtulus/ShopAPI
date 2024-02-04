--Shop is my database name.I call database for adding tables
use Shop
--User_Role table
create table User_Role(
id int identity(1,1) primary key,
roleName nvarchar(15)
)
--Shop_User table
create table Shop_User(
id int identity(1,1) primary key,
userName nvarchar(20),
userPass nvarchar(20),
fullName nvarchar(50),
userAddress nvarchar(250),
roleId int foreign key references User_Role(id)
)
--Product_Type table
create table Product_Type(
id int identity(1,1) primary key,
typeName nvarchar(20)
)
--Product Table
create table Product(
id int identity(1,1) primary key,
productName nvarchar(50),
productId int foreign key references Product_Type(id),
stock int,
price int,
imageUrl nvarchar(max)
)
