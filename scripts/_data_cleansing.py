import pandas as pd
import re
import os


def load_data(file_path):
    """Load data from any CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded file with {len(df)} rows and {len(df.columns)} columns.")
        return df
    except Exception as e:
        raise ValueError(f"Failed to load the file: {e}")


def handle_missing_values(df):
    """Handle missing values in the dataset."""
    print("Handling missing values...")
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].fillna("Unknown")
    return df


def remove_duplicates(df):
    """Remove duplicate rows."""
    print("Removing duplicates...")
    return df.drop_duplicates()


def clean_string_columns(df):
    """Clean string columns: trim whitespace and remove leading/trailing spaces."""
    print("Cleaning string columns...")
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].str.strip()
    return df


def standardize_column_names(df):
    """Standardize column names to snake_case."""
    print("Standardizing column names...")
    df.columns = [re.sub(r'\s+', '_', col).lower() for col in df.columns]
    return df


def normalize_data_types(df):
    """Normalize data types for better consistency."""
    print("Normalizing data types...")
    for col in df.select_dtypes(include=['object']).columns:
        if "zip" in col or "zipcode" in col:
            df[col] = df[col].astype(str).str.zfill(5)  # Standardize ZIP codes to 5 digits
    return df


def split_address(df):
    """Split address into components if 'address' column exists."""
    if 'address' not in df.columns:
        print("No 'address' column found. Skipping address splitting.")
        return df

    print("Splitting address into components...")

    def split_address_logic(address):
        try:
            parts = address.split(", ")
            street = parts[0] if len(parts) > 0 else None
            city = parts[1] if len(parts) > 1 else None
            state_zip = parts[2].split(" ") if len(parts) > 2 else [None, None]
            state = state_zip[0]
            zip_code = state_zip[1] if len(state_zip) > 1 else None
            zip_code = zip_code.zfill(5) if zip_code and zip_code.isdigit() else zip_code
            return pd.Series([street, city, state, zip_code])
        except Exception as e:
            print(f"Error splitting address: {address} -> {e}")
            return pd.Series([None, None, None, None])

    df[['street', 'city', 'state', 'zip']] = df['address'].apply(split_address_logic)
    df = df.drop(columns=['address'])  # Drop the original 'address' column
    return df


def save_data(df, output_path):
    """Save the cleaned data to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        raise ValueError(f"Failed to save the file: {e}")


def clean_data(file_path, output_dir):
    """
    End-to-end data cleaning pipeline.

    Args:
        file_path (str): Path to the input data file.
        output_dir (str): Directory to save the cleaned file.
    """
    # Load the data
    df = load_data(file_path)

    # Data cleaning steps
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = clean_string_columns(df)
    df = standardize_column_names(df)
    df = normalize_data_types(df)
    df = split_address(df)

    # Save the cleaned data
    output_file = os.path.join(output_dir, "cleaned_data.csv")
    save_data(df, output_file)


if __name__ == "__main__":
    # Input and output paths
    input_file = r"C:\Users\Admin\PycharmProjects\etl_gcp\data_cleaning_scripts\dataset\emp_data.csv"
    output_directory = r"C:\Users\Admin\PycharmProjects\etl_gcp\data_cleaning_scripts\dataset"

    # Run the data cleaning pipeline
    clean_data(input_file, output_directory)
