from django.shortcuts import render
from .models import EconomicEvent


def home(request):
    return render(request, 'core/home.html', {
        'email_address': 'kojrey@kojreycodes.com'
    })


def event_list(request):
    events = EconomicEvent.objects.all()
    
    # Get any stored messages from the session
    success_message = request.session.pop('success_message', None)
    error_message = request.session.pop('error_message', None)
    
    return render(request, 'core/event_list.html', {
        'events': events,
        'success_message': success_message,
        'error_message': error_message,
        'email_address': 'kojrey@kojreycodes.com'
    })
