from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    account_no = models.BigIntegerField(primary_key=True)

class Transaction(models.Model):

    transaction_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="sender_account")
    receiver = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="receiver_account")
    amount = models.FloatField()
    datetime = models.DateTimeField(auto_created=True)



