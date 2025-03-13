from django.urls import path
from . import views

urlpatterns = [
    # Add paths for integration-related views here
    path('fetch-events/', views.fetch_events, name='fetch_events'),
    path('clear-events/', views.clear_events, name='clear_events'),
] 