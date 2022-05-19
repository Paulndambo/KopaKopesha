from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("members", views.MemberViewSet, basename="members")

urlpatterns = [ 
    path("", include(router.urls)),
    path("users-list/", views.UsersListAPIView.as_view(), name="users-list"),
]