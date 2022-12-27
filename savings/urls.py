from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("savings-list", views.SavingViewSet, basename="savings-list")

urlpatterns= [ 
    path("", include(router.urls)),
    path("transactions/", views.TransactionListCreateAPIView.as_view(), name="transactions"),
    path("member/<int:member_id>/transactions", views.MemberTransactionsListAPIView.as_view(), name="member-transactions"),
    #path("user-savings/<int:user_id>/", views.UserSavingsAPIView.as_view(), name="user-savings"),
]