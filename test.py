import pandas as pd

# Sample DataFrame
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28]
}

df_main = pd.DataFrame(data)

# Function Definition with Type Handling
def vlookup(df_main, lookup_value, lookup_column, return_column):
    if lookup_column not in df_main.columns or return_column not in df_main.columns:
        raise ValueError("Specified columns are not in the dataframe")
    
    # Ensure the lookup_value type matches the type of the lookup_column
    try:
        lookup_value = type(df_main[lookup_column].iloc[0])(lookup_value)
    except ValueError as e:
        raise ValueError(f"Type conversion error: {e}")

    result = df_main.loc[df_main[lookup_column] == lookup_value, return_column]
    if result.empty:
        return None
    else:
        return result.iloc[0]

# Example Usage
lookup_value = '3'  # Intentionally using a string to demonstrate type conversion
lookup_column = 'ID'
return_column = 'Name'

result = vlookup(df_main, lookup_value, lookup_column, return_column)
print(result)  # Output: Charlie
