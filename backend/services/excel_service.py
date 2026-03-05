import pandas as pd


def read_excel_file(file_path: str) -> pd.DataFrame:
    """
    Reads an Excel file and returns a DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")


def validate_data(df: pd.DataFrame, required_columns: list) -> bool:
    """
    Validates the DataFrame to ensure all required columns are present.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return True


def get_dataframes_from_excel(file_path: str, required_columns: list) -> pd.DataFrame:
    """
    Reads an Excel file, validates its data, and returns a DataFrame.
    """
    df = read_excel_file(file_path)
    validate_data(df, required_columns)
    return df
