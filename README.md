
## Retail Store Database Management System
![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/82a1be5c-aba1-4ffc-8f27-62569b58f675)

### Overview

This script provides a set of functionalities to manage a retail store database using MySQL. It allows users to insert data into `locations` and `countries` tables, perform various queries on customer and order data, and generate reports on sales and customer spending.

### Prerequisites

- Python 3
- `mysql-connector-python` package
- MySQL server with an accessible database

### Installation

1. Install the required Python package:
    ```bash
    pip install mysql-connector-python
    ```
2. Ensure that your MySQL server is running and you have the necessary credentials to connect to the `retail_store` database.

### How to Run

1. Start the script:
    ```bash
    python safertekexam.py
    ```
2. Follow the on-screen instructions to perform various operations.

### Script Functionalities

#### Database Connection

The script connects to the MySQL server using the provided credentials. It creates necessary tables if they do not already exist:
- `Customers`
- `Products`
- `Orders`
- `OrderItems`

#### Menu Options

1. **List All Customers**
![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/7d6fa7a2-edba-454f-b89e-5e6571ba4d5f)

   - Retrieves and displays all records from the `Customers` table.
![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/842a457d-36ff-4d59-8261-6a71958da671)


3. **Find January 2023 Orders**
   - Retrieves and displays all orders placed in January 2023 from the `Orders` table.

4. **Get Order Details**
   - Retrieves and displays details of all orders, including customer information, by joining `Orders` and `Customers` tables.

5. **List Products in an Order**
   - Prompts the user to enter an order ID and retrieves the products and quantities in that order by joining `OrderItems` and `Products` tables.

6. **Calculate Total Amount Spent by Each Customer**
   - Calculates and displays the total amount spent by each customer by joining `Customers`, `Orders`, `OrderItems`, and `Products` tables.

7. **Find the Most Popular Product**
   - Finds and displays the most popular product based on the total quantity sold by joining `OrderItems` and `Products` tables.

8. **Get Monthly Sales in 2023**
    - Retrieves and displays the total number of orders and sales amount for each month in 2023 by joining `Orders`, `OrderItems`, and `Products` tables.

9. **Find Customers Who Spent More Than $1000**
    - Retrieves and displays customers who have spent more than $1000 by joining `Customers`, `Orders`, `OrderItems`, and `Products` tables.

### Error Handling

The script includes error handling to catch and display MySQL errors. It ensures that the database connection and cursor are closed properly in the `finally` block.

### Usage Notes

- Modify the MySQL connection parameters (`host`, `user`, `password`, `database`) as per your setup.
- Ensure that the `retail_store` database exists before running the script.
- The script prompts the user for inputs where necessary and displays the results of queries on the console.
