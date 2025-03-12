from django.shortcuts import render
from .models import EconomicEvent


def event_list(request):
    events = EconomicEvent.objects.all()
    return render(request, 'core/event_list.html', {'events': events})
