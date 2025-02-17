from typing import Dict, Optional, List
import requests
from config.config import Config


class FREDClient:
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        self.session.params = self.config.DEFAULT_PARAMS

    def get_series_info(self, series_id: str) -> Dict:
        """
        Fetch metadata for a given series ID.
        """
        endpoint = f"{self.config.BASE_URL}/series"
        params = {
            'series_id': series_id
        }

        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def get_series(self, series_id: str, **kwargs) -> Dict:
        """
        Fetch time series data for a given series ID.

        Args:
            series_id (str): FRED series identifier
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dict: Combined series metadata and observations
        """
        # Get series metadata
        series_info = self.get_series_info(series_id)

        # Get observations
        endpoint = f"{self.config.BASE_URL}/series/observations"
        params = {
            'series_id': series_id,
            **kwargs
        }

        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        observations_data = response.json()

        # Combine metadata and observations
        return {
            **series_info,
            'observations': observations_data['observations']
        }

    def search_series(self, search_text: str, **kwargs) -> Dict:
        """
        Search for series matching the given text.

        Args:
            search_text (str): Text to search for
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dict: JSON response containing search results
        """
        endpoint = f"{self.config.BASE_URL}/series/search"
        params = {
            'search_text': search_text,
            **kwargs
        }

        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
