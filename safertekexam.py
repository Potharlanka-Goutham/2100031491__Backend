import mysql.connector

def insert_location_data(cur):
    print("Enter Location table data:")
    print()
    street_address = input("Enter street address: ")
    city = input("Enter city: ")
    state_province = input("Enter state/province: ")
    country_id = input("Enter country code: ")
    print()
    sql = "INSERT INTO locations (street_address, city, state_province, country_id) VALUES (%s, %s, %s, %s)"
    val = (street_address, city, state_province, country_id)
    cur.execute(sql, val)

def insert_country_data(cur):
    print("Enter Countries table data:")
    print()
    country_id = input("Enter country ID: ")
    country_name = input("Enter country Name: ")
    region_id = input("Enter region id: ")
    print()
    sql = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
    val = (country_id, country_name, region_id)
    cur.execute(sql, val)

def find_address(cur):
    country_name = input("Enter country name to apply join condition on that country name: ")
    cur.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name, c.country_id
                   FROM locations l
                   JOIN countries c ON l.country_id = c.country_id
                   WHERE c.country_name = %s''', (country_name,))
    rows = cur.fetchall()
    print()
    for row in rows:
        print(row)
    print()

# Define functions for the retail store queries
def list_all_customers(cur):
    cur.execute('SELECT * FROM Customers')
    customers = cur.fetchall()
    print("Customers:")
    for customer in customers:
        print(customer)
    print()

def find_january_orders(cur):
    cur.execute('SELECT * FROM Orders WHERE OrderDate LIKE "2023-01%"')
    january_orders = cur.fetchall()
    print("January 2023 Orders:")
    for order in january_orders:
        print(order)
    print()

def order_details(cur):
    cur.execute('''
    SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, Customers.Email, Orders.OrderDate
    FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    ''')
    order_details = cur.fetchall()
    print("Order Details:")
    for detail in order_details:
        print(detail)
    print()

def products_in_order(cur):
    order_id = input("Enter OrderID: ")
    cur.execute('''
    SELECT Products.ProductName, OrderItems.Quantity
    FROM OrderItems
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    WHERE OrderItems.OrderID = %s
    ''', (order_id,))
    order_products = cur.fetchall()
    print(f"Products in Order {order_id}:")
    for product in order_products:
        print(product)
    print()

def total_spent_by_customers(cur):
    cur.execute('''
    SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent
    FROM Customers
    JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Customers.CustomerID
    ''')
    total_spent = cur.fetchall()
    print("Total Amount Spent by Each Customer:")
    for amount in total_spent:
        print(amount)
    print()

def most_popular_product(cur):
    cur.execute('''
    SELECT Products.ProductID, Products.ProductName, SUM(OrderItems.Quantity) AS TotalQuantity
    FROM OrderItems
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Products.ProductID
    ORDER BY TotalQuantity DESC
    LIMIT 1
    ''')
    most_popular_product = cur.fetchone()
    print("Most Popular Product:")
    print(most_popular_product)
    print()

def monthly_sales_2023(cur):
    cur.execute('''
    SELECT DATE_FORMAT(Orders.OrderDate, '%Y-%m') AS Month, COUNT(Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSales
    FROM Orders
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    WHERE Orders.OrderDate LIKE '2023-%'
    GROUP BY DATE_FORMAT(Orders.OrderDate, '%Y-%m')
    ''')
    monthly_sales = cur.fetchall()
    print("Total Orders and Sales Amount for Each Month in 2023:")
    for month in monthly_sales:
        print(month)
    print()

def customers_spent_more_than_1000(cur):
    cur.execute('''
    SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent
    FROM Customers
    JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Customers.CustomerID
    HAVING TotalSpent > 1000
    ''')
    big_spenders = cur.fetchall()
    print("Customers who have spent more than $1000:")
    for spender in big_spenders:
        print(spender)
    print()

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8204",
        database="retail_store"
    )
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Customers (
                    CustomerID INT PRIMARY KEY,
                    FirstName VARCHAR(50),
                    LastName VARCHAR(50),
                    Email VARCHAR(100),
                    DateOfBirth DATE
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Products (
                    ProductID INT PRIMARY KEY,
                    ProductName VARCHAR(100),
                    Price DECIMAL(10, 2)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Orders (
                    OrderID INT PRIMARY KEY,
                    CustomerID INT,
                    OrderDate DATE,
                    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS OrderItems (
                    OrderItemID INT PRIMARY KEY,
                    OrderID INT,
                    ProductID INT,
                    Quantity INT,
                    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                )''')

    actions = {
        '1': insert_location_data,
        '2': insert_country_data,
        '3': find_address,
        '4': list_all_customers,
        '5': find_january_orders,
        '6': order_details,
        '7': products_in_order,
        '8': total_spent_by_customers,
        '9': most_popular_product,
        '10': monthly_sales_2023,
        '11': customers_spent_more_than_1000
    }

    while True:
        print("Select an option:")
        print("1. Insert Location Data")
        print("2. Insert Countries Data")
        print("3. Find Address")
        print("4. List All Customers")
        print("5. Find January 2023 Orders")
        print("6. Get Order Details")
        print("7. List Products in an Order")
        print("8. Calculate Total Amount Spent by Each Customer")
        print("9. Find the Most Popular Product")
        print("10. Get Monthly Sales in 2023")
        print("11. Find Customers Who Spent More Than $1000")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == '12':
            break

        action = actions.get(choice)
        if action:
            action(cur)
            conn.commit()
        else:
            print("Invalid choice!")

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
