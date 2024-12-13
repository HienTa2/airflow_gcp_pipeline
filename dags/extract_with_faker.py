from faker import Faker
import random

# Specify the number of employees to generate
num_employees = 10

# Create Faker instance
fake = Faker()

# Employee data structure (with password and salary)
employee_data = []

for _ in range(num_employees):
    employee = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job_title": fake.job(),
        "department": fake.company(),
        "email": fake.email(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "password": fake.password(length=10),  # Generate a random password
        "salary": round(random.uniform(50000, 150000), 2)  # Generate a salary between $50k and $150k
    }
    employee_data.append(employee)

# Print or export the generated data
for emp in employee_data:
    print(emp)

# If you want to export this data to a file, you can use pandas
# Uncomment the code below to save as a CSV
"""
import pandas as pd
df = pd.DataFrame(employee_data)
df.to_csv('employee_data.csv', index=False)
print("Employee data saved to employee_data.csv")
"""
