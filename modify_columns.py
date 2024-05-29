def add_column(df, column_name, data):
    df[column_name] = data
    return df

def remove_column(df, column_name):
    if column_name in df.columns:
        df.drop(columns=[column_name], inplace=True)
    else:
        print(f"Error: Column {column_name} does not exist.")
    return df
