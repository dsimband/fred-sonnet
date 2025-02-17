from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Observation:
    date: datetime
    value: float


@dataclass
class Series:
    id: str
    title: str
    frequency: str
    units: str
    observations: List[Observation]
    notes: Optional[str] = None

    @classmethod
    def from_api_response(cls, response: dict) -> 'Series':
        """
        Create a Series object from the FRED API response.

        Expected response format:
        {
            'realtime_start': '...',
            'realtime_end': '...',
            'observation_start': '...',
            'observation_end': '...',
            'units': '...',
            'output_type': '...',
            'file_type': 'json',
            'order_by': '...',
            'sort_order': '...',
            'count': ...,
            'offset': ...,
            'limit': ...,
            'observations': [
                {
                    'realtime_start': '...',
                    'realtime_end': '...',
                    'date': '...',
                    'value': '...'
                },
                ...
            ]
        }
        """
        observations = []
        for obs in response['observations']:
            try:
                value = float(obs['value']) if obs['value'] != '.' else None
                observations.append(
                    Observation(
                        date=datetime.strptime(obs['date'], '%Y-%m-%d'),
                        value=value
                    )
                )
            except (ValueError, TypeError):
                # Skip observations with invalid values
                continue

        return cls(
            # Handle both direct and search responses
            id=response.get('seriess', [{}])[0].get('id', '') or '',
            title=response.get('seriess', [{}])[0].get('title', '') or '',
            frequency=response.get('seriess', [{}])[
                0].get('frequency', '') or '',
            units=response.get('seriess', [{}])[0].get('units', '') or '',
            observations=observations,
            notes=response.get('notes', '')
        )
