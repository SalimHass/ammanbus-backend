from django.urls import path
from django.urls import path, include
from rest_framework import routers
from accounts import views

# from accounts.api.viewsets import DriverDashBoardViewSet, PassengersDashBoardViewSet


router = routers.DefaultRouter()
# router.register(r'driver-dashboard', DriverDashBoardViewSet)
# router.register(r'passenger-dashboard', PassengersDashBoardViewSet)

router.register(r'register', views.AccountViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('register/', include('rest_framework.urls', namespace='rest_framework')),

]