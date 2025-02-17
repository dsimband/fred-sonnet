# tests/test_economic_data.py
import pytest
from datetime import datetime
from src.models.economic_data import Series, Observation


def test_series_from_api_response(sample_series_response):
    """Test creating a Series object from API response."""
    series = Series.from_api_response(sample_series_response)

    assert series.id == 'GDP'
    assert len(series.observations) == 2
    assert isinstance(series.observations[0].date, datetime)
    assert isinstance(series.observations[0].value, float)
    assert series.observations[0].value == 25723.9
