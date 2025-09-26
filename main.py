
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
    occupations = df[df.columns[1]].combine_first(df[df.columns[0]])

    # Drop non-month columns
    df = drop_non_months(df)

    # Add the occupations column back to the DataFrame
    df['occupations'] = occupations

    # Convert all columns except 'occupations' to numeric
    df = convert_to_numeric(df, 'occupations')

    # Group by occupations values and sum numeric columns
    df_grouped = df.groupby('occupations').sum()

    # Keep only the last 24 columns (plus 'occupations' if present)
    cols_to_keep =  list(df_grouped.columns[-50:])
    df_grouped = df_grouped[cols_to_keep]

    # Drop rows where the index (occupations) does not match a four-digit code
    df_filtered = drop_non_occupation_rows(df_grouped)

    print('Final DataFrame:')
    print(df_filtered)

    df_filtered.to_excel('data/processed_output.xlsx', index=True)


if __name__ == "__main__":
    main()