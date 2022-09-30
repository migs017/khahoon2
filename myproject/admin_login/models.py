from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.conf import settings

# Create your models here.
#dito yung mga models na mag iinteract sa database
#meta not sure sa use ng meta pero dun dinedeclare yung table
#every time may babaguhin dito sa models.py run niyo to para magamit siya sa db: 
# py manage.py makemigrations
# py manage.py migrate
#pag gumamit ng django may default tables isa na don ang Auth_user dun nag iistore yung mga user at maganda siya gamitin since my built in function like
#login(),create_user() etc.

# class user(models.Model):
#     # username = models.TextField(max_length=20)
#     # password = models.TextField(max_length=20)

#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

#     class Meta:
#         db_table = 'user'

#     def __str__(self):
#         return self.Name

class inventory(models.Model):
    # id = models.IntegerField()
    productName = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return self.Name
    def item_total(self):
        return self.quantity*self.price

class message(models.Model):
    # userId = models.ForeignKey(User,null=True,on_delete=models.CASCADE) #pwede to
    sender = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='sender') #pero mas updated yata tong User, Kung ano name ng variable yun ang pang call sa select ex: msg.userId.username
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    thread = models.IntegerField()
    receiver = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='receiver')#foreignkey(table_name,null=True,on_delete=models.CASCADE)
    class Meta:
        db_table = 'message'
    
    def __str__(self):
        # me = User.objects.filter(self.sender)
        # return self.me
        return self.message
        # return self.sender+""+self.subject+""+self.message+""+self.date+""+self.thread+""+self.receiver

    def getSender(self):
        me = User.objects.filter(self.sender)
        return self.me
        