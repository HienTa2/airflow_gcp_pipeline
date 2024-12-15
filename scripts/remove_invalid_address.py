import pandas as pd

# Load your data into a pandas DataFrame
# Assuming you have a CSV file with a column named "address"
df = pd.read_csv("emp_data.csv")

# Define keywords to filter out invalid addresses
invalid_keywords = ["PO Box", "FPO", "APO", "DPO", "USNS", "USS", "USNV"]

# Create a function to check for invalid addresses
def is_valid_address(address):
    return not any(keyword in address for keyword in invalid_keywords)

# Filter the DataFrame
df_cleaned = df[df["address"].apply(is_valid_address)]

# Save the cleaned data to a new CSV file
df_cleaned.to_csv("cleaned_emp_data.csv", index=False)

print("Cleaned data saved to 'cleaned_emp_data.csv'.")
