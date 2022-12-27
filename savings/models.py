from django.db import models

# Create your models here.
class Saving(models.Model):
    member = models.OneToOneField(to="users.Member", on_delete=models.DO_NOTHING, related_name="savings")
    balance = models.FloatField(default=0)
    
    def __str__(self):
        return self.member.first_name

TRANSACTION_TYPES = (
    ("deposit", "Deposit"),
    ("withdraw", "Withdraw"),
)

class Transaction(models.Model):
    member = models.ForeignKey(to="users.Member", on_delete=models.CASCADE, related_name="transactions")
    type = models.CharField(max_length=200, choices=TRANSACTION_TYPES)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.first_name


    