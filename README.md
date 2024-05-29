# DataFrame Operations and Visualization Tool

This project provides a tool for performing various operations and visualizations on a CSV file using a DataFrame. The tool is modularized into several Python modules, each handling different aspects of the functionality.

## Modules

## Modules

- `file_reader`: Contains functions for reading CSV files.
- `input_parser`: Provides functions for parsing user input.
- `operations`: Includes functions for performing various operations on DataFrames, such as arithmetic operations, filtering, summarizing, etc.
- `visualization`: Contains functions for visualizing data using different chart types.
- `save_csv`: Provides a function for saving DataFrames to CSV files.
- `filter_data`: Includes functions for filtering data based on column conditions.
- `summarize_data`: Provides functions for computing summary statistics of DataFrame.
- `correlation`: Contains functions for computing and visualizing correlation matrix.
- `modify_columns`: Includes functions for adding and removing columns from DataFrame.


# DataFrame Operations

This Python script performs various operations on DataFrame objects from CSV files. It offers functionalities such as performing arithmetic operations, filtering data, visualizing data, summarizing data, and more.

## Features

- Read CSV file
- Perform arithmetic operations on DataFrame columns or individual cells
- Filter data based on column conditions
- Visualize data using different chart types
- Summarize data statistics
- Compute and visualize correlation matrix
- Add and remove columns from DataFrame
- Save modified DataFrame to a new CSV file


## Instructions

- When prompted, enter the operation you want to perform in the specified format.
- Use `exit` to terminate the program.

### Operation Formats

- Arithmetic operation between columns: `column1 + column2`, `column1 - column2`, etc.
- Arithmetic operation between individual cells: `0,A + 1,B`, etc.
- Filter data: `FILTER(column condition)`
- Summary statistics: `SUMMARY`
- Correlation matrix visualization: `CORRELATION`
- Save DataFrame to CSV file: `SAVE(path)`
- Add new column to DataFrame: `ADD(column, data)`
- Remove column from DataFrame: `REMOVE(column)`
- Visualize data: `VISUALIZE(chart_type, column1, column2)`
- Single DataFrame operation: `DF_SINGLE_OP(df, value, operation)`
- VLOOKUP operation: `VLOOKUP(value, lookup_col, result_col)`


## Requirements

- Python 3.7 or higher
- pandas
- matplotlib
- seaborn


