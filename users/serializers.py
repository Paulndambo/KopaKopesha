from rest_framework import serializers
from .models import Member, User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "first_name", "last_name", "id_number", "phone_number", "membership", "postal_code", "zip_code", "town", "country"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]