# google-calendar-economic-events

A Django application that fetches Economic Calendar events from an API and syncs them with Google Calendar.

## Features

- Fetch Economic Calendar events (earnings, dividends, etc.) from API
- User authentication and authorization
- Google Calendar integration
- Customizable event selection
- Automated calendar syncing

## Requirements

- Python 3.10
- Django 4.2.7
- Other dependencies listed in requirements.txt

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/google-calendar-economic-events.git
cd google-calendar-economic-events
```

2. Create and activate a virtual environment:
```bash
python -m venv calapp
source calapp/bin/activate  # On Windows use: calapp\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with the following variables:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
ALPHA_VANTAGE_API_KEY=your-alpha-vantage-api-key
GOOGLE_OAUTH_CLIENT_ID=your-google-oauth-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-google-oauth-client-secret
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Log in to the application
2. Configure your Alpha Vantage API settings
3. Authorize Google Calendar access
4. Select the financial events you want to track
5. Sync events to your calendar

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
