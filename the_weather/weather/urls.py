from django.urls import path
from . import views 
#/Users/rodo/Desktop/python_tutorials/python django/
# weather_app/the_weather/weather/templates/weather/weather.html

urlpatterns = [
    path('',views.index),
]

