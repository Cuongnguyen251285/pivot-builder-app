import pandas as pd

class FilterService:
    @staticmethod
    def filter_dataframe(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Filters the DataFrame based on given keyword arguments where keys are column names and values are the corresponding filter values.
        """
        for key, value in kwargs.items():
            if key in df.columns:
                df = df[df[key] == value]
        return df

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
# filtered_df = FilterService.filter_dataframe(df, A=2)  # Returns DataFrame with A=2
