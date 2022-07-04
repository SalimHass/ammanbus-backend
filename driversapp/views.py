from django.shortcuts import render
from rest_framework import viewsets
from .api.serializers import DriverAppSerializer
from .models import DriverApp
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


from rest_framework import  permissions
# Create your views here.

class DriverAppView(viewsets.ModelViewSet):
    serializer_class = DriverAppSerializer
    queryset = DriverApp.objects.all()
    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


