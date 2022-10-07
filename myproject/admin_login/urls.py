from django.urls import path,include

from . import views
#dito yung mga urls ng website
urlpatterns = [
    path('', views.index, name='index',),#path(name sa website,name sa views,di ko pa alam)
    path('Dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('Add_client', views.add_client, name='add_client'),
    path('Inquiry', views.inquiry, name='inquiry'),
    path('inquiryView/<int:num>', views.inquiryView, name='inquiryView'),
    path('Inventory', views.inventory_view, name='inventory'),
    path('Forecast', views.forecast, name='forecast'),
    path('POS', views.pos, name='pos'),
    # path('sign',views.sign,),
]