# def save_csv_file(df, file_path):
#     try:
#         df.to_csv(file_path, index=False)
#         print(f"DataFrame saved to {file_path}")
#     except Exception as e:
#         print(f"Error: Could not save DataFrame to {file_path}. {e}")


import os

def save_csv_file(df, file_name=None):
    try:
        if file_name is None:
            file_name = input("Enter the file name (without extension): ")
        file_path = os.path.join(os.getcwd(), f"{file_name}.csv")
        df.to_csv(file_path, index=False)
        print(f"DataFrame saved to {file_path}")
    except Exception as e:
        print(f"Error: Could not save DataFrame to {file_path}. {e}")