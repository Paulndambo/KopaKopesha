from django.db import models

from users.models import Member

# Create your models here.
class Saving(models.Model):
    member = models.OneToOneField(Member, on_delete=models.DO_NOTHING)
    balance = models.FloatField(default=0)
    
    def __str__(self):
        return self.member.first_name

TRANSACTION_TYPES = (
    ("deposit", "Deposit"),
    ("withdraw", "Withdraw"),
)

class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=TRANSACTION_TYPES)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    