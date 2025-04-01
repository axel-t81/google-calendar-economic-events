from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .utils import fetch_earnings_events
from core.models import EconomicEvent
import json
from datetime import datetime, timedelta
import uuid

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

def download_events(request):
    """
    View to download selected events as .ics file.
    Accepts a POST request with event IDs in JSON format.
    Returns an .ics file for download.
    
    Note: The dates are already corrected when stored in the database during
    the fetch_earnings_events process, so no adjustment is needed here.
    """
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'}, status=405)
    
    try:
        # Parse request body
        data = json.loads(request.body)
        event_ids = data.get('event_ids', [])
        
        if not event_ids:
            return JsonResponse({'success': False, 'message': 'No events selected.'}, status=400)
            
        # Get events from database
        events = EconomicEvent.objects.filter(id__in=event_ids)
        
        if not events:
            return JsonResponse({'success': False, 'message': 'No events found.'}, status=404)
        
        # Generate .ics content
        ics_content = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "PRODID:-//Earnings Calendar//EN",
            "CALSCALE:GREGORIAN",
            "METHOD:PUBLISH"
        ]
        
        for event in events:
            # Create a unique identifier for the event
            uid = str(uuid.uuid4())
            
            # Format start and end date (assuming events last 1 hour)
            start_date = event.date
            end_date = event.date
            
            # Format dates for iCalendar
            start_str = start_date.strftime("%Y%m%d")
            end_str = end_date.strftime("%Y%m%d")
            
            # Create event entry
            ics_content.extend([
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"SUMMARY:{event.name}",
                f"DESCRIPTION:{event.description or ''}",
                f"DTSTART;VALUE=DATE:{start_str}",
                f"DTEND;VALUE=DATE:{end_str}",
                f"LOCATION:{event.company}",
                "END:VEVENT"
            ])
            
        ics_content.append("END:VCALENDAR")
        
        # Join with CRLF as per iCalendar spec
        ics_data = "\r\n".join(ics_content)
        
        # Create response with appropriate headers
        response = HttpResponse(ics_data, content_type='text/calendar')
        response['Content-Disposition'] = 'attachment; filename="earnings-events.ics"'
        
        return response
        
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
