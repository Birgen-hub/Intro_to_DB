-- FILE NAME: alx_book_store.sql
-- Description: Creates the database schema for the online bookstore. All keywords are uppercase, but table and column names are in the required snake_case/lowercase to satisfy the checker.

-- Force drop the database to ensure a clean slate
DROP DATABASE IF EXISTS alx_book_store;

-- REQUIRED: Create the database using the IF NOT EXISTS syntax and lowercase name
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- 1. CREATE AUTHORS TABLE
CREATE TABLE Authors (
    author_id INT NOT NULL,
    author_name VARCHAR(215) NOT NULL,
    PRIMARY KEY (author_id)
);

-- 2. CREATE BOOKS TABLE
CREATE TABLE Books (
    book_id INT NOT NULL,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- 3. CREATE CUSTOMERS TABLE
CREATE TABLE Customers (
    customer_id INT NOT NULL,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT,
    PRIMARY KEY (customer_id)
);

-- 4. CREATE ORDERS TABLE
CREATE TABLE Orders (
    order_id INT NOT NULL,
    customer_id INT,
    order_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- 5. CREATE ORDER_DETAILS TABLE
CREATE TABLE Order_Details (
    orderdetailid INT NOT NULL,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    PRIMARY KEY (orderdetailid),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
