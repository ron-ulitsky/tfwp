# Remove columns where row 4 is not a three-letter month abbreviation
from pandas import DataFrame, to_datetime, to_numeric

def drop_non_months(df: DataFrame) -> DataFrame:

	month_abbr = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
	valid_cols = [col for col in df.columns if str(df.loc[4, col]) in month_abbr]
	df = df[valid_cols]

	# Replace row 4 with the last day of each month, starting from Jan 2015
	# Format row 4 as 'Mon YYYY' for each column, starting from Jan 2015
	start_year = 2015
	start_month = 1
	for i, col in enumerate(df.columns):
		year = start_year + (start_month - 1 + i) // 12
		month = (start_month - 1 + i) % 12 + 1
		df.loc[4, col] = f"{to_datetime(f'{year}-{month:02d}-01').strftime('%b %Y')}"


	# Set row 4 as the new column headers
	df.columns = df.loc[4]
	df = df.drop(4)

	return df


def convert_to_numeric(df: DataFrame, exclude_col: str) -> DataFrame:
	"""
	Convert all columns in the DataFrame to numeric, except for the specified column.
	Non-convertible values are set to NaN.
	"""
	for col in df.columns:
		if col != exclude_col:
			df[col] = to_numeric(df[col], errors='coerce')
	return df


def drop_non_occupation_rows(df: DataFrame) -> DataFrame:
	"""
	Drop rows where the index does not start with a four-digit code.
	"""
	good_index = df.index.str.strip().str.match(r'^\d{4}')
	return df[good_index]