from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .utils import fetch_earnings_events
from core.models import EconomicEvent

# Create your views here.

def fetch_events(request):
    """
    View to fetch earnings events from Alpha Vantage.
    If the request is AJAX, returns JSON response.
    Otherwise, redirects to the event list page with a message.
    """
    result = fetch_earnings_events()
    
    # Check if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(result)
    
    # If not AJAX, store message in session and redirect
    if result['success']:
        request.session['success_message'] = result['message']
    else:
        request.session['error_message'] = result['message']
    
    return redirect('event_list')

def clear_events(request):
    """
    View to clear all events from the database.
    If the request is AJAX, returns JSON response.
    Otherwise, redirects to the event list page with a message.
    """
    try:
        count = EconomicEvent.objects.count()
        EconomicEvent.objects.all().delete()
        result = {
            'success': True,
            'message': f"Successfully cleared {count} events."
        }
    except Exception as e:
        result = {
            'success': False,
            'message': f"Error clearing events: {str(e)}"
        }
    
    # Check if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(result)
    
    # If not AJAX, store message in session and redirect
    if result['success']:
        request.session['success_message'] = result['message']
    else:
        request.session['error_message'] = result['message']
    
    return redirect('event_list')
