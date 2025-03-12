import requests
import os
from core.models import EconomicEvent

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def fetch_economic_events():
    url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Assuming the data is in a format that can be iterated over
        for item in data.get('earningsCalendar', []):
            event, created = EconomicEvent.objects.get_or_create(
                name=item.get('name'),
                date=item.get('date'),
                defaults={'description': item.get('description', '')}
            )
            if not created:
                event.description = item.get('description', '')
                event.save()
    else:
        print("Failed to fetch data from Alpha Vantage") 