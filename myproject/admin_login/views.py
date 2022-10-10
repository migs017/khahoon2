import re
from urllib import request
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.template import loader
from django.contrib.auth import logout as django_logout
from .forms import addClient
from .forms import updateInventory
from .models import inventory,message,transaction, transaction_products
from itertools import chain
from django.contrib.auth.decorators import login_required
# Create your views here.
#eto yung controller ng system
#yung (request) is default base sa understanding ko
#is_valid is connected sa forms.py doon nag seset ng form validation
#render() eto yung nag sshow ng html which is nasa templates
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password)

        if user is not None:
            auth.login(request , user)
                
            if request.user.is_staff and request.user.is_authenticated:
                request.session['username'] = username = request.POST['username']
                return redirect('dashboard')
                
            else:
                messages.error(request, 'User is not a staff')
                return redirect("index")
                
        else:
            messages.error(request, 'Invalid username or password')
            return redirect("index")
    else:
        return render(request,'login.html')
    
    
@login_required
def dashboard(request):
    template = loader.get_template('admin_dashboard.html')
    return HttpResponse(template.render())

@login_required
def add_client(request):
    if request.method == "POST":
        form = addClient(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            messages.success(request, "Successfully created")
            User.objects.create_user(email=email,username=username,password=password,is_staff=True)
            # user = User.objects.create_user(email=email,username=username,password=password,is_staff=True)
            return redirect('add_client')
        # else:
            # print('ey')
            # form = addClient()
    else:
        form = addClient()
    return render(request,'add_client.html',{'form':form})  

@login_required
def inquiry(request):
    template = loader.get_template('admin_inquiry.html')
    # message_obj = message.objects.all()
    # message_obj = message.objects.values('sender','subject','message','date','receiver','thread').distinct('thread')
    message_obj = message.objects.distinct('thread')
    context = {"message_details":message_obj}
    return HttpResponse(template.render(context,request))
    
    # message_obj = User.objects.all()
    # return HttpResponse(message_obj)

    # message_obj = message.objects.all()
    # return HttpResponse(message_obj)
    # return HttpResponse('ey')
@login_required
def inquiryView(request,num=2):
    # working add message na lang
    template = loader.get_template('admin_reply.html')
    msg = message.objects.filter(thread=num)
    sender = User.objects.filter(username=request.session['username'])
    # context = {"message_details":messages}
    # # return HttpResponse(template.render(context,request))
    if request.method == "POST":
        msg = message.objects.filter(id=1)
        data = request.POST
        info = data.get("mes")
        for md in msg:
            temp = message(sender_id=request.session['_auth_user_id'],subject=md.subject,message=info,receiver_id=md.sender_id,thread=md.thread)
            temp.save()
        messages.success(request, "Sent")
        return redirect('inquiry')
        # return HttpResponse(messages)
    else:
        return HttpResponse(template.render({"message_details":msg,"sender_details":sender},request))
    # return HttpResponse(messages)
    # return HttpResponse('ey')

def pos(request):
    template = loader.get_template('admin_pos.html')
    transaction_obj = transaction.objects.all()
    context = {"transaction_details":transaction_obj}

    if request.method == "POST":
        data = request.POST
        tid = data.get("transaction_id")

        return redirect('Transactions/'+tid, tid=tid)
    else:

        return HttpResponse(template.render(context,request))

#View_transaction
def view_transaction(request, tid):
    template = loader.get_template('admin_view_transactions.html')
    products_obj = transaction_products.objects.all()
    transaction_obj = transaction.objects.all()
    context = {"prod_details":products_obj, "transaction_details":transaction_obj, 'tid':tid}

    return HttpResponse(template.render(context,request))


def inventory_view(request):
    template = loader.get_template('admin_inventory.html')
    inventory_obj = inventory.objects.all()
    context = {"item_details":inventory_obj}
    

    if request.method == "POST":
        
        data = request.POST
        quantity = data.get("u_quantity")
        price = data.get("u_price")
        pid = data.get("productID")
        print(quantity, price, pid)
        messages.success(request, "Successfully updated")
        
        inventory.objects.filter(id=pid).update(quantity = quantity, price = price)
        


        # user = User.objects.create_user(email=email,username=username,password=password,is_staff=True)
        return HttpResponse(template.render(context,request))

    else:
        return HttpResponse(template.render(context,request))
@login_required
def forecast(request):
    template = loader.get_template('admin_forecast.html')
    return HttpResponse(template.render())

    # inventory_obj = inventory.objects.all()
    # return HttpResponse(inventory_obj)

def forecast_view(request):
    template = loader.get_template('admin_forecast.html')
    qty = transaction_products.objects.filter(t_date = '2022-10-09')
    transaction_obj = transaction.objects.all()
    context = {"transact":transaction_obj, "qty": qty}
    return HttpResponse(template.render(context,request))
    
def register(request):
    if request.method == 'POST':
        # email = request.POST['email']
        # password= request.POST['password']

        # user = User.objects.create_user(password = password , email = email)
        # user.save()
        # print('user created')
        # return redirect('index')
        form = User(request.POST)
        
        if request.method == 'POST':
            form.save()

    return render(request,'register.html')

def home(request):
    users_obj = User.objects.all()
    context = {"user_details":users_obj}
    return render(request, 'test.html',context)
