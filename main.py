
import pandas as pd
from utils import drop_non_months, convert_to_numeric, drop_non_occupation_rows


def main():
    # Load the Excel file
    # Retrieved 25 Sept 2025 from
    # https://open.canada.ca/data/en/dataset/360024f2-17e9-4558-bfc1-3616485d65b9/resource/c78d5eb3-9644-42c4-9c04-02dad020ea53
    file_path = 'data/EN_ODP-TR-Work-TFWP_PT_NOC4_sign.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl', header=None)

    # Coalesce values in columns 0 and 1
    # These columns contain occupation codes and names, with some missing values
    occupation = df[df.columns[1]].combine_first(df[df.columns[0]])

    # Drop non-month columns
    df = drop_non_months(df)

    # Add the occupation column back to the DataFrame
    df['occupation'] = occupation

    # Convert all columns except 'occupation' to numeric
    df = convert_to_numeric(df, 'occupation')

    # Group by occupation values and sum numeric columns
    df_grouped = df.groupby('occupation').sum()

    # Drop rows where the index (occupation) does not match a four-digit code
    df_filtered = drop_non_occupation_rows(df_grouped)

    # Sort df_filtered by the sum of each row (descending)
    df_filtered = df_filtered.assign(_sum=df_filtered.sum(axis=1)).sort_values('_sum', ascending=False).drop('_sum', axis=1)

    print('Final DataFrame:')
    print(df_filtered)

    # Save the processed DataFrame to an Excel file
    print('Saving processed DataFrame to data/processed_output.xlsx')
    df_filtered.to_excel('data/processed_output.xlsx', index=True)
    print('Done!')


if __name__ == "__main__":
    main()