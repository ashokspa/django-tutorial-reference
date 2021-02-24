from django.urls import path
from AppOne import views

urlpatterns = [
    path('',views.index,name="index")
]