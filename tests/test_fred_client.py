# tests/test_fred_client.py
import pytest
import responses
from src.api.fred_client import FREDClient


@responses.activate
def test_get_series(fred_client, sample_series_response):
    """Test fetching a series from FRED."""
    # Mock the API response
    responses.add(
        responses.GET,
        'https://api.stlouisfed.org/fred/series/observations',
        json=sample_series_response,
        status=200
    )

    response = fred_client.get_series('GDP')
    assert response == sample_series_response
    assert len(responses.calls) == 1


@responses.activate
def test_search_series(fred_client):
    """Test searching for series in FRED."""
    mock_response = {
        'seriess': [
            {
                'id': 'UNRATE',
                'title': 'Unemployment Rate',
                'frequency': 'Monthly'
            }
        ]
    }

    responses.add(
        responses.GET,
        'https://api.stlouisfed.org/fred/series/search',
        json=mock_response,
        status=200
    )

    response = fred_client.search_series('unemployment')
    assert response == mock_response
    assert len(responses.calls) == 1
