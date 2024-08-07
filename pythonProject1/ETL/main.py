import pandas as pd
import requests
from lxml import etree

# Step 1: Download the XML file from the URL
url = 'https://data.ny.gov/api/views/nacg-rg66/rows.xml?accessType=DOWNLOAD'
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    try:
        # Step 2: Parse the XML file and convert it into a DataFrame
        # Use lxml to parse the XML content
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.fromstring(response.content, parser)

        # Read the XML into a DataFrame using pandas
        df = pd.read_xml(response.content, xpath='.//row', parser='lxml')

        # Step 3: Display the structure of the DataFrame
        print("Available columns in the DataFrame:")
        print(df.columns)

        print("Data types in the DataFrame:")
        print(df.dtypes)

        print("First few rows of the DataFrame:")
        print(df.head())

        # Step 4: Handle missing data
        print("Missing data in the DataFrame before cleaning:")
        print(df.isnull().sum())

        # Remove column with many missing values
        if 'tax_liability_of_nontaxable_returns_in_thousands' in df.columns:
            df.drop(columns=['tax_liability_of_nontaxable_returns_in_thousands'], inplace=True)

        # Remove rows with missing values in specific columns
        df.dropna(subset=['tax_liability_of_taxable_returns_in_thousands', 'average_tax_of_taxable_returns'], inplace=True)

        # Fill remaining missing data with default values
        df.fillna({
            'tax_year': 0,
            'resident_type': 'unknown',
            'place_of_residence': 'unknown',
            'country': 'unknown',
            'state': 'unknown',
            'county': 'unknown',
            'number_of_all_returns': 0,
            'ny_agi_of_all_returns_in_thousands': 0,
            'tax_liability_of_all_returns_in_thousands': 0,
            'number_of_taxable_returns': 0,
            'ny_agi_of_taxable_returns_in_thousands': 0,
            'number_of_nontaxable_returns': 0,
            'ny_agi_of_nontaxable_returns_in_thousands': 0,
            'average_ny_agi_of_all_returns': 0,
            'average_tax_of_all_returns': 0,
            'average_ny_agi_of_taxable_returns': 0,
            'average_tax_of_taxable_returns': 0,
            'average_ny_agi_of_nontaxable_returns': 0,
            'county_sort_order': 0
        }, inplace=True)

        # Convert numeric columns that should be of integer type
        for column in df.select_dtypes(include=['float64']).columns:
            df[column] = df[column].fillna(0).astype(int)

        # Check the changes made
        print("Missing data in the DataFrame after cleaning:")
        print(df.isnull().sum())

        # Save the cleaned DataFrame to a CSV file
        df.to_csv('tax_data_cleaned_v6.csv', index=False)
        print("Cleaned data saved to 'tax_data_cleaned_v6.csv'.")

    except ValueError as e:
        print(f"Error reading XML: {e}")
else:
    print(f"Error downloading the XML file. Status code: {response.status_code}")
