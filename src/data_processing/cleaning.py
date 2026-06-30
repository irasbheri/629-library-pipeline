"""Data cleaning functions for library pipeline.

The cleaning module
This module contains functions for cleaning and standardizing data.
All functions return new DataFrames without modifying the input.
"""

# Uncomment when needed:
# import pandas as pd
# from typing import List, Optional

import logging

logger = logging.getLogger(__name__)


def remove_duplicates(df, subset=None):
    """Remove duplicate rows from DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame
        subset (list, optional): Columns to consider for duplicates

    Returns:
        pd.DataFrame: DataFrame with duplicates removed

    Example:
        >>> df_clean = remove_duplicates(df, subset=['transaction_id'])
    """
    df = df.copy()  # Work on a copy!

    initial_rows = len(df)
    df = df.drop_duplicates(subset=subset, keep='first')
    removed = initial_rows - len(df)

    if removed > 0:
        print(f"######################## Removed {removed} duplicate rows")
        logger.info(f"Removed {removed} duplicate rows")

    return df


def handle_missing_values(df, strategy='drop', fill_value=None, columns=None):
    """Handle missing values in DataFrame."""
    df = df.copy()
    return df


def standardize_dates(df, date_columns, date_format='%Y-%m-%d'):
    """Standardize date columns to consistent format."""
    df = df.copy()
    return df
