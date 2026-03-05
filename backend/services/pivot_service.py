import pandas as pd

class PivotService:
    def __init__(self, data):
        self.data = data

    def generate_pivot_table(self, index, values, aggfunc='sum'):
        """Generate a pivot table.
        
        Args:
            index (list): The keys to group by on the pivot table index.
            values (list): The values to aggregate.
            aggfunc (str): The aggregation function to use (default is 'sum').
        """
        return pd.pivot_table(self.data, index=index, values=values, aggfunc=aggfunc)

    def aggregate(self, group_by, agg_funcs):
        """Aggregate data based on group by and given aggregation functions.
        
        Args:
            group_by (list): The keys to group by.
            agg_funcs (dict): A dictionary of column names and their respective aggregation functions.
        """
        return self.data.groupby(group_by).agg(agg_funcs)