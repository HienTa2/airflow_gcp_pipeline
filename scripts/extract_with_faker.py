from faker import Faker
import random
import pandas as pd

# Specify the number of employees to generate
num_employees = 100

# Create Faker instance
fake = Faker()

# Employee data structure
employee_data = []

for _ in range(num_employees):
    employee = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job_title": fake.job(),
        "department": fake.company(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),  # Replace newlines with commas
        "phone_number": fake.numerify("###-###-####"),  # Standardize phone number format
        "password": fake.password(length=10),  # Generate a random password
        "salary": round(random.uniform(50000, 150000), 2),  # Salary between $50k and $150k
    }
    employee_data.append(employee)

# Export to CSV with proper escaping
df = pd.DataFrame(employee_data)

# Save the CSV with no quotes but handle special characters safely
df.to_csv(
    'employee_data.csv',
    index=False,
    sep=',',  # Use comma as the separator
    quoting=0,  # Use csv.QUOTE_MINIMAL
    escapechar='\\',  # Escape special characters
    encoding='utf-8'  # Ensure proper encoding
)
print("Employee data saved to employee_data.csv")
