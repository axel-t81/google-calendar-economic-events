# earnings-calendar-to-google-calendar

A Django application that fetches Earnings events from an API and syncs them with Google Calendar.

## Features

- Fetch Earnings events from API
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
git clone https://github.com/yourusername/earnings-calendar-to-google-calendar.git
cd earnings-calendar-to-google-calendar
```

2. Create and activate a virtual environment:
```bash
python -m venv yourenvname
source yourenvname/bin/activate  # On Windows use: yourenvname\Scripts\activate
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

1. Visit Site
2. Fetch the earnings events you want to track
5. Sync events to your Google Calendar

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
