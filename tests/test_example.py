"""Example test to demonstrate pytest.

Copy this pattern for your own tests!
"""

import pytest
import pandas as pd


@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    })


def test_example_len(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3

def test_example_id(sample_df):
    """Example test - shows pytest working."""
    assert 'id' in sample_df.columns

def test_example_name(sample_df):
    """Example test - shows pytest working."""
    assert 'name' in sample_df.columns

def test_example_col_not_present(sample_df):
    """Example test - shows pytest working."""
    assert 'startDate' not in sample_df.columns

def test_example_unique(sample_df):
    """Example test - shows pytest working."""
    assert sample_df['id'].is_unique
