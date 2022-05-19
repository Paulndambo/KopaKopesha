from django.shortcuts import render

from savings.models import Saving, Transaction
from .serializers import TransactionSerializer, SavingSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
# Create your views here.
class SavingViewSet(viewsets.ModelViewSet):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = self.serializer_class(instance=transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)