from django.urls import path,include
from . import views
#dito yung mga urls ng website
urlpatterns = [
    path('', views.index, name='index',),#path(name sa website,name sa views,di ko pa alam)
    path('Login', views.index, name='index',),
    path('Logout', views.logout, name='logout'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('Add_client', views.add_client, name='add_client'),
    path('Inquiry', views.inquiry, name='inquiry'),
    path('inquiryView/<int:num>', views.inquiryView, name='inquiryView'),
    path('Transactions/<int:tid>', views.view_transaction, name='view_transaction'),
    path('Forecast', views.forecast_view, name='forecast_view'),
    path('Inventory', views.inventory_view, name='inventory'),
    path('POS', views.pos, name='pos'),
    path('forecast', views.forecast, name='forecast'),
    # path('sign',views.sign,),
]