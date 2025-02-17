# tests/conftest.py
import pytest
from src.api.fred_client import FREDClient

@pytest.fixture
def fred_client():
    """Provides a FRED client instance for testing."""
    return FREDClient()

@pytest.fixture
def sample_series_response():
    """Provides a sample FRED API series response."""
    return {
        'series_id': 'GDP',
        'title': 'Gross Domestic Product',
        'frequency': 'Quarterly',
        'units': 'Billions of Dollars',
        'observations': [
            {'date': '2023-01-01', 'value': '25723.9'},
            {'date': '2023-04-01', 'value': '26047.2'}
        ]
    }