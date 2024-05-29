def filter_data(df, column, condition):
    try:
        filtered_df = df.query(f"{column} {condition}")
        return filtered_df
    except Exception as e:
        print(f"Error: Could not filter data. {e}")
        return df
