from .models import Coupon, Get, Vehicle, View, Location
from .serializers import CouponSerializer, GetSerializer, VehicleSerializer, ViewSerializer,LocationSerializer
from django.views.generic import ListView,DetailView,TemplateView, CreateView
from Coupon.models import Get,Coupon







class ViewCoupon(TemplateView):
   template_name = "coupon.html"
   def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        G = Get.objects.get(username=self.request.user.username)
        print(G.coup_id)
        if G.coup_id.coup_id == 1:
            coupid = 1
        else:
            coupid = 2
        context={'q':coupid,'obj':G}
        return context



class ViewRedeemCoupon(TemplateView):
   template_name = "coupon.html"
   def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        G = Get.objects.get(username=self.request.user.username)
        G.status = False
        G.save()
        r = True
        print(G.coup_id)
        if G.coup_id.coup_id == 1:
            coupid = 1
        else:
            coupid = 2
        context={'q':coupid,'obj':G,'r':r}
        return context