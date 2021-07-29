from rest_framework import serializers
from .models import Coupon, Get, Vehicle, Location, View

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('coup_id',
                  'coup_name',
                  'start_date',
                  'end_date',
                  'count')

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Get
        fields = ('gid',
                  'coup_id',
                  'cid',
                  'coupon_unique_code')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vid',
                  'vtype',
                  'status')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('locid',
                  'ltype')
    
class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ('viewid',
                  'locid',
                  'cid')