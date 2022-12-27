from django.shortcuts import render, get_object_or_404
from django.conf import settings
User = settings.AUTH_USER_MODEL
from savings.models import Saving, Transaction
from users.models import Member
from .serializers import TransactionSerializer, SavingSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class SavingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = self.serializer_class(instance=transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        member = request.data['member']
        type = request.data['type'].lower()
        amount = float(request.data['amount'])
        serializer = self.serializer_class(data=data)
        
        savings = Saving.objects.get(member=member)
        if serializer.is_valid():
            if type == "deposit":
                savings.balance = savings.balance + amount
                savings.save()
            elif type == "withdraw":
                savings.balance = savings.balance - amount
                savings.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberTransactionsListAPIView(generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, member_id):
        member = get_object_or_404(Member, pk=member_id)
        transactions = Transaction.objects.filter(member=member)
        serializer = self.serializer_class(instance=transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSavingsAPIView(generics.GenericAPIView):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer

    def get(self, request):
        user_id = request.data['user_id']
        member = Member.objects.get(user__id=user_id)
        savings = Saving.objects.filter(member=member)
        serializer = self.serializer_class(instance=savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
