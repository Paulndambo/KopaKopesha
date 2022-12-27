from django.shortcuts import render
from .models import Member, User
from .serializers import MemberSerializer, UserSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from savings.serializers import SavingSerializer, MemberTransactionSerializer
from rest_framework.decorators import action
from savings.models import Saving, Transaction
# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


    def perform_create(self, serializer):
        user = self.request.user
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        id_number = serializer.validated_data.get('id_number')
        phone_number = serializer.validated_data.get('phone_number')
        #membership = serializer.validated_data.get('membership')
        postal_code = serializer.validated_data.get('postal_code')
        zip_code = serializer.validated_data.get('zip_code')
        town = serializer.validated_data.get('town')
        country = serializer.validated_data.get('country')

        print(user)

        
        serializer.save(
            user=user, first_name=first_name, 
            last_name=last_name, id_number=id_number, 
            phone_number=phone_number,
            postal_code=postal_code, zip_code=zip_code,
            town=town, country=country
        ) 
        
        return Response({"success": "Member Created Successfully"})


class MemberProfileModelViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=["get", "GET"], url_path="savings", url_name="savings")
    def get_member_savings(self, request, pk=None):
        member_savings = Saving.objects.filter(member_id=pk)
        serializer = SavingSerializer(instance=member_savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get", "GET"], url_path="transactions", url_name="transactions")
    def get_member_transactions(self, request, pk=None):
        member_transactions = Transaction.objects.filter(member_id=pk)
        serializer = MemberTransactionSerializer(instance=member_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UsersListAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
