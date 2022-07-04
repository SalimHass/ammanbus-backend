#from email import message
#from django.shortcuts import render, redirect
#from django.contrib.auth import login, logout,authenticate, get_user_model
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib import messages
from .api.serializers import AccountSerializer
#from django.views.generic import CreateView
from .models import Account
#from .forms import PassengerSignUpForm, DriverSignUpForm

from rest_framework import viewsets, status, permissions

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]