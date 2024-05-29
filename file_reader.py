import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.ParserError:
        print("Error: Could not parse the CSV file.")
        return None
    except UnicodeDecodeError as e:
        print(f"Error: {e}")
        return None
