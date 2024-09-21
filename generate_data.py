# We can generate the data by ourselves using pandas
# Here are the below steps by which we can generate all CSV files for our project:

import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Function to generate random orders data
def generate_orders(num_orders):
    orders_data = {
        "OrderID": range(1, num_orders + 1),
        "CustomerID": [random.randint(1, 100) for _ in range(num_orders)],  # 100 unique customers
        "OrderDate": [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_orders)],
        "FulfillmentDate": [
            datetime.now() - timedelta(days=random.randint(1, 30)) if random.random() > 0.2 else None
            for _ in range(num_orders)
        ],
        "OrderAmount": [round(random.uniform(10, 1000), 2) for _ in range(num_orders)],
        "Status": [random.choice(["Fulfilled", "Pending", "Cancelled"]) for _ in range(num_orders)]
    }
    
    orders_df = pd.DataFrame(orders_data)
    return orders_df

# Function to generate random customers data
def generate_customers(num_customers):
    customers_data = {
        "CustomerID": range(1, num_customers + 1),
        "FirstName": [f"FirstName{i}" for i in range(1, num_customers + 1)],
        "LastName": [f"LastName{i}" for i in range(1, num_customers + 1)],
        "Email": [f"customer{i}@example.com" for i in range(1, num_customers + 1)],
        "Region": [random.choice(["North", "South", "East", "West"]) for _ in range(num_customers)],
        "NPSScore": [random.randint(1, 10) for _ in range(num_customers)]
    }
    
    customers_df = pd.DataFrame(customers_data)
    return customers_df

# Function to generate random financials data
def generate_financials(num_years):
    financials_data = {
        "FinancialYear": [2023 - i for i in range(num_years)],
        "TotalRevenue": [random.randint(300000, 800000) for _ in range(num_years)],
        "CostOfGoodsSold": [random.randint(150000, 600000) for _ in range(num_years)],
        "OperatingExpenses": [random.randint(50000, 200000) for _ in range(num_years)]
    }
    
    financials_df = pd.DataFrame(financials_data)
    return financials_df

# Create a directory for the data
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Parameters
num_orders = 10000  # Number of orders
num_customers = 1000  # Number of customers
num_years = 5  # Number of financial years

# Generate data
orders_df = generate_orders(num_orders)
customers_df = generate_customers(num_customers)
financials_df = generate_financials(num_years)

# Save all data to separate CSV files in the same folder
orders_df.to_csv(f"{data_dir}/orders_large.csv", index=False)
customers_df.to_csv(f"{data_dir}/customers_large.csv", index=False)
financials_df.to_csv(f"{data_dir}/financials_large.csv", index=False)

print("Data generation complete! Files saved in the 'data' folder.")
