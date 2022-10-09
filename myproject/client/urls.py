from django.urls import path,include

from . import views
#dito yung mga urls ng website
urlpatterns = [
    path('Dashboard', views.client_dashboard, name='client-dashboard'),
]