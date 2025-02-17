from typing import List
import pandas as pd
from src.models.economic_data import Series


def series_to_dataframe(series: Series) -> pd.DataFrame:
    """
    Convert a Series object to a pandas DataFrame.

    Args:
        series (Series): Series object containing economic data

    Returns:
        pd.DataFrame: DataFrame with date index and values
    """
    data = {
        'date': [obs.date for obs in series.observations],
        'value': [obs.value for obs in series.observations]
    }
    df = pd.DataFrame(data)
    df.set_index('date', inplace=True)
    return df
