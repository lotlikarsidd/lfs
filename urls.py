from django.conf.urls import url
from .models import Coupon, Get, Vehicle, View, Location
from .serializers import CouponSerializer, GetSerializer, VehicleSerializer, ViewSerializer,LocationSerializer
from .views import ViewRedeemCoupon,ViewCoupon
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   
    path('coupon/<str:pk>/',ViewCoupon.as_view()),
    path('coupon/redeem/<str:pk>/',ViewRedeemCoupon.as_view())
]