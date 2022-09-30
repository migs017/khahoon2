import re
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.template import loader
from .forms import addClient
from .models import inventory,message
from itertools import chain
from django.db.models.expressions import RawSQL
# Create your views here.
#eto yung controller ng system
#yung (request) is default base sa understanding ko
#is_valid is connected sa forms.py doon nag seset ng form validation
#render() eto yung nag sshow ng html which is nasa templates
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('dashboard')    
        else:
            messages.error(request, 'invalid username or password')
            return redirect("index")
    else:
        return render(request,'login.html')
def dashboard(request):
    template = loader.get_template('admin_dashboard.html')
    return HttpResponse(template.render())

def add_client(request):
    if request.method == "POST":
        form = addClient(request.POST)
        if form.is_valid():
            print ('yow') #pangtest
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

def inquiry(request):
    template = loader.get_template('admin_inquiry.html')
    message_obj = message.objects.all()
    context = {"message_details":message_obj}
    return HttpResponse(template.render(context,request))
    
    # message_obj = User.objects.all()
    # return HttpResponse(message_obj)

    # message_obj = message.objects.all()
    # return HttpResponse(message_obj)
    # return HttpResponse('ey')

def inquiryView(request,num=2):
    # working add message na lang
    template = loader.get_template('admin_reply.html')
    messages = message.objects.filter(id=num)
    context = {"message_details":messages}
    # # return HttpResponse(template.render(context,request))
    if request.method == "POST":
        messages = message.objects.filter(id=1)
        data = request.POST
        info = data.get("mes")
        for md in messages:
            temp = message(sender_id='1',subject=md.subject,message=info,receiver_id=md.sender_id,thread=md.thread)
            temp.save()
        messages.success(request, "Sent")
        return redirect('inquiry')
        # return HttpResponse(messages)
    else:
        return HttpResponse(template.render(context,request))
    # return HttpResponse(messages)
    # return HttpResponse('ey')

def pos(request):
    template = loader.get_template('admin_pos.html')
    inventory_obj = inventory.objects.all()
    context = {"item_details":inventory_obj}
    return HttpResponse(template.render(context,request))


def inventory_view(request):
    template = loader.get_template('admin_inventory.html')
    inventory_obj = inventory.objects.all()
    context = {"item_details":inventory_obj}
    return HttpResponse(template.render(context,request))

    # inventory_obj = inventory.objects.all()
    # return HttpResponse(inventory_obj)
    
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