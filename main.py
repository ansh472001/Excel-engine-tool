import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from file_reader import read_csv_file
from input_parser import parse_user_input
from operations import perform_operation, perform_series_operation, perform_single_dataframe_operation, vlookup
from visualization import visualize_data
from save_csv import save_csv_file
from filter_data import filter_data
from summarize_data import summarize_data
from correlation import visualize_correlation_matrix
from modify_columns import add_column, remove_column

def main():
    df = read_csv_file('Sample_data.csv')
    if df is None:
        return
    
    print("Initial DataFrame:\n", df)

    try:
        start_row = int(input("Enter start row label: "))
        end_row = int(input("Enter end row label: "))
        start_column = input("Enter start column label: ")
        end_column = input("Enter end column label: ")

        new_df = df.loc[start_row:end_row, start_column:end_column].copy()
        print("Extracted DataFrame:\n", new_df)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
        return

    while True:
    
        user_input = input("\n\nEnter the operation\n\n (e.g., '0,A + 1,B', 'A + B', 'FILTER(column condition)', 'SUMMARY', 'CORRELATION', 'SAVE', 'ADD(column, data)', 'REMOVE(column)')\n\n 'VLOOKUP(value, lookup_col, result_col)'\n\n 'VISUALIZE(chart_type, column1, column2)'\n\n 'DF_SINGLE_OP(df, value, operation)'\n\n: ")
        if user_input.lower() == 'exit':
            break
        try:
            if user_input.startswith('VLOOKUP'):
                pattern = re.compile(r"VLOOKUP\(([^,]+),([^,]+),([^,]+)\)")
                match = pattern.match(user_input.strip())
                if match:
                    lookup_value = match.group(1).strip()
                    lookup_col = match.group(2).strip()
                    result_col = match.group(3).strip()
                    result = vlookup(new_df, lookup_value, lookup_col, result_col)
                    if result is not None:
                        print(f"VLOOKUP result for value '{lookup_value}' in column '{lookup_col}': {result}")
                    else:
                        print(f"No match found for value '{lookup_value}' in column '{lookup_col}'.")
                else:
                    print("Error: Invalid format for VLOOKUP command.")
            elif user_input.startswith('VISUALIZE'):
                pattern = re.compile(r'VISUALIZE\(([^,]+),([^,]+)?(?:,([^,]+))?\)')
                match = pattern.match(user_input.strip())
                if match:
                    chart_type = match.group(1).strip().strip("'\"")
                    column1 = match.group(2).strip().strip("'\"") if match.group(2) else None
                    column2 = match.group(3).strip().strip("'\"") if match.group(3) else None
                    visualize_data(new_df, chart_type, column1, column2)
                else:
                    print("Error: Invalid format for VISUALIZE command.")
            elif user_input.startswith('DF_SINGLE_OP'):
                pattern = re.compile(r'DF_SINGLE_OP\(([^,]+),([^,]+),([^,]+)\)')
                match = pattern.match(user_input.strip())
                if match:
                    df_name = match.group(1).strip()
                    value = float(match.group(2).strip())
                    operation = match.group(3).strip().strip("'\"")
                    result_df = perform_single_dataframe_operation(new_df, value, operation)
                    if result_df is not None:
                        print(f"Result of {operation} operation on DataFrame with value {value} is:\n{result_df}")
                else:
                    print("Error: Invalid format for DF_SINGLE_OP command.")
            elif user_input.startswith('FILTER'):
                pattern = re.compile(r'FILTER\(([^,]+) (.+)\)')
                match = pattern.match(user_input.strip())
                if match:
                    column = match.group(1).strip()
                    condition = match.group(2).strip()
                    new_df = filter_data(new_df, column, condition)
                    print(f"Filtered DataFrame:\n{new_df}")
                else:
                    print("Error: Invalid format for FILTER command.")
            elif user_input.startswith('SUMMARY'):
                print(f"Data Summary:\n{summarize_data(new_df)}")
            elif user_input.startswith('CORRELATION'):
                visualize_correlation_matrix(new_df)
            elif user_input.startswith('SAVE'):
                # pattern = re.compile(r'SAVE\(([^)]+)\)')
                # match = pattern.match(user_input.strip())
                # if match:
                    # save_path = match.group(1).strip().strip("'\"")
                save_csv_file(new_df)
                # else:
                    # print("Error: Invalid format for SAVE command.")
            elif user_input.startswith('ADD'):
                pattern = re.compile(r'ADD\(([^,]+),(.+)\)')
                match = pattern.match(user_input.strip())
                if match:
                    column_name = match.group(1).strip().strip("'\"")
                    data = eval(match.group(2).strip())
                    new_df = add_column(new_df, column_name, data)
                    print(f"Updated DataFrame with new column {column_name}:\n{new_df}")
                else:
                    print("Error: Invalid format for ADD command.")
            elif user_input.startswith('REMOVE'):
                pattern = re.compile(r'REMOVE\(([^)]+)\)')
                match = pattern.match(user_input.strip())
                if match:
                    column_name = match.group(1).strip().strip("'\"")
                    new_df = remove_column(new_df, column_name)
                    print(f"Updated DataFrame with column {column_name} removed:\n{new_df}")
                else:
                    print("Error: Invalid format for REMOVE command.")
            elif ',' in user_input and any(op in user_input for op in '+-*/><=!'):
                cell1, cell2, operation = parse_user_input(user_input)
                result = perform_operation(new_df, cell1, cell2, operation)
                if result is not None:
                    print(f"Result of {operation} between cell ({cell1[0]}, {cell1[1]}) and cell ({cell2[0]}, {cell2[1]}) is: {result}")
            elif any(op in user_input for op in '+-*/><='):
                column1, operation, column2 = re.split(r'(\+|\-|\*|\/|>|<|>=|<=|==|!=)', user_input)
                column1 = column1.strip()
                operation = operation.strip()
                column2 = column2.strip()
                result = perform_series_operation(new_df, column1, column2, operation)
                print(f"Result of {operation} operation between series {column1} and {column2} is:\n{result}")
            else:
                print("Error: Invalid input format.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
