from django.urls import path

from .views import *

app_name = "parameter"

urlpatterns = [
    path('get/getProvince', getProvince, name='getProvince'),
    path('get/getDistrict', getDistrict, name='getDistrict'),

]
