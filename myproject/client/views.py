from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def client_dashboard(request):
    template = loader.get_template('client_dashboard.html')
    return HttpResponse(template.render())

