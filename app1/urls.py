from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('kohli/',kohli,name='kohli'),
]