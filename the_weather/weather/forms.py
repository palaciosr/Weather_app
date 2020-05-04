from django.forms import ModelForm, TextInput
from .models import City 

class CityForm(ModelForm):

    class Meta:

        model= City 

        fields =['name']
        widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}


#https://github.com/PrettyPrinted/weather_app_django/blob/master/the_weather/weather/views.py