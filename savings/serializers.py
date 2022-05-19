from rest_framework import serializers
from .models import Saving, Transaction

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"