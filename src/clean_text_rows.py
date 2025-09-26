import pandas as pd

def clean_text_rows_na(df, replace_value=''):
    text_columns = df.select_dtypes(include=['object']).columns

    for column in text_columns:
        df[column] = (
            df[column]
            .fillna(replace_value)
            .astype(str)
        )
    
    return df
