import pandas as pd

def perform_operation(df, cell1, cell2, operation):
    val1 = df.at[cell1[0], cell1[1]]
    val2 = df.at[cell2[0], cell2[1]]

    if operation == '+':
        result = val1 + val2
    elif operation == '-':
        result = val1 - val2
    elif operation == '*':
        result = val1 * val2
    elif operation == '/':
        if val2 != 0:
            result = val1 / val2
        else:
            result = None
            print("Error: Division by zero.")
    elif operation == '>':
        result = val1 > val2
    elif operation == '<':
        result = val1 < val2
    elif operation == '==':
        result = val1 == val2
    elif operation == '!=':
        result = val1 != val2
    elif operation == '>=':
        result = val1 >= val2
    elif operation == '<=':
        result = val1 <= val2
    else:
        result = None
        print("Error: Invalid operation.")
    
    return result

def perform_series_operation(df, column1, column2, operation):
    series1 = df[column1]
    series2 = df[column2]

    if operation == '+':
        result = series1 + series2
    elif operation == '-':
        result = series1 - series2
    elif operation == '*':
        result = series1 * series2
    elif operation == '/':
        result = series1 / series2
    elif operation == '>':
        result = series1 > series2
    elif operation == '<':
        result = series1 < series2
    elif operation == '==':
        result = series1 == series2
    elif operation == '!=':
        result = series1 != series2
    elif operation == '>=':
        result = series1 >= series2
    elif operation == '<=':
        result = series1 <= series2
    else:
        result = None
        print("Error: Invalid operation.")
    
    return result

def perform_single_dataframe_operation(df, value, operation):
    if operation == '+':
        result = df + value
    elif operation == '-':
        result = df - value
    elif operation == '*':
        result = df * value
    elif operation == '/':
        result = df / value
    else:
        result = None
        print("Error: Invalid operation.")
    
    return result

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

# def perform_column_arithmetic(df, column, value, operation):

#     if operation not in ('+', '-', '*', '/'):
#         raise ValueError("Invalid operation. Supported operations are '+', '-', '*', '/'.")

#     try:
#         if operation == '+':
#             result = df[column] + value
#         elif operation == '-':
#             result = df[column] - value
#         elif operation == '*':
#             result = df[column] * value
#         elif operation == '/':
#             result = df[column] / value
#     except KeyError:
#         raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

#     return result
