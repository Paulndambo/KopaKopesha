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

    """
    def create(self, validated_data):
        member = validated_data['member']
        print(member)
    """

class MemberTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "type", "amount", "created_at"]