from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("savings-list", views.SavingViewSet, basename="savings-list")

urlpatterns= [ 
    path("", include(router.urls)),
    path("transactions/", views.TransactionListCreateAPIView.as_view(), name="transactions"),
]