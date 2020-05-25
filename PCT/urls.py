from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.index, name="index"),
    path('scan/',views.scan, name="scan"),
    path('update/',views.update, name="update"),


    path('add_record/<str:v_iid>/',views.add_record, name="add_record"),
    path('cheak_record/<str:v_iid>/',views.cheak_record, name="cheak_record"),
]
