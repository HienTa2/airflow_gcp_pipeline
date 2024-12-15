import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\etl_gcp\data_cleaning_scripts\dataset\cleaned_emp_data.csv")

# Function to split address into components
def split_address(address):
    try:
        # Split into address, city, state+zip
        parts = address.split(", ")
        street_address = parts[0]  # The first part is the street address
        city = parts[1]           # The second part is the city
        state_zip = parts[2].split(" ")  # Split state and zip by space
        state = state_zip[0].strip()     # The first part is the state, remove extra spaces
        zip_code = state_zip[1].strip()  # The second part is the ZIP code, remove extra spaces
        return pd.Series([street_address, city, state, zip_code])
    except IndexError:
        # If the address doesn't match the expected format, return NaN
        return pd.Series([None, None, None, None])

# Apply the split_address function to the 'address' column
df[['Street Address', 'City', 'State', 'ZIP Code']] = df['address'].apply(split_address)

# Strip any trailing or leading spaces in all string columns, particularly ZIP Code
df['ZIP Code'] = df['ZIP Code'].str.strip()

# Drop the original 'address' column if needed
df.drop(columns=['address'], inplace=True)

# Save the cleaned data with separate columns
df.to_csv(r"C:\Users\Admin\PycharmProjects\etl_gcp\data_cleaning_scripts\dataset\split_addresses_cleaned.csv", index=False)

print("Address has been split into separate columns and saved to 'split_addresses_cleaned.csv'.")
