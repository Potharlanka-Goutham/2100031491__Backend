
## Retail Store Database Management System

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


2. **Find January 2023 Orders**
   -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/e389a81c-2277-46dd-938d-415edbd9ed99)

   - Retrieves and displays all orders placed in January 2023 from the `Orders` table.
   - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/1f2b296e-362c-42ea-b129-4f0b89c61fa2)

     

3. **Get Order Details**
   -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/43b360bc-6e36-457c-9406-4ed056ca2fca)

   - Retrieves and displays details of all orders, including customer information, by joining `Orders` and `Customers` tables.
   - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/5b209e10-894a-4a8c-8d7f-f107fc00cd2b)


4. **List Products in an Order**
   -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/04eb2406-b5d9-499d-bc28-315a7b65f75d)

   - Prompts the user to enter an order ID and retrieves the products and quantities in that order by joining `OrderItems` and `Products` tables.
   - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/115cbc92-7951-4e3f-8769-6162b9740b6b)


5. **Calculate Total Amount Spent by Each Customer**
   -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/d2f5b74c-0484-4201-a56c-c78019048312)

   - Calculates and displays the total amount spent by each customer by joining `Customers`, `Orders`, `OrderItems`, and `Products` tables.
   - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/047cbb50-0db2-4123-9fef-7cc1e5f5a9a9)


6. **Find the Most Popular Product**
   -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/255b4c5e-5535-42d1-a66c-093d49b66f79)

   - Finds and displays the most popular product based on the total quantity sold by joining `OrderItems` and `Products` tables.
   - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/1fd36da2-e3ac-49f1-8f6a-2c2af85bd596)


7. **Get Monthly Sales in 2023**
    -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/19262dff-5ecb-4d0c-b18b-57323764881c)

    - Retrieves and displays the total number of orders and sales amount for each month in 2023 by joining `Orders`, `OrderItems`, and `Products` tables.
    - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/efd465fb-0d9d-4a2d-aafa-c14d65ca0f0c)


8. **Find Customers Who Spent More Than $1000**
    -![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/aede369f-842f-4edd-8a71-b62b98c178dd)

    - Retrieves and displays customers who have spent more than $1000 by joining `Customers`, `Orders`, `OrderItems`, and `Products` tables.
    - ![image](https://github.com/Potharlanka-Goutham/2100031491__Backend/assets/110443146/14f25a84-b6c6-45cb-994c-d5378fdc36ed)


### Error Handling

The script includes error handling to catch and display MySQL errors. It ensures that the database connection and cursor are closed properly in the `finally` block.

### Usage Notes

- Modify the MySQL connection parameters (`host`, `user`, `password`, `database`) as per your setup.
- Ensure that the `retail_store` database exists before running the script.
- The script prompts the user for inputs where necessary and displays the results of queries on the console.
