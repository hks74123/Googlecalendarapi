from django.urls import path
from . import views

urlpatterns = [
    path('restv1/calendar/init/', views.GoogleCalendarInitView),
    path('rest/v1/calendar/redirect/', views.GoogleCalendarRedirectView),
]
