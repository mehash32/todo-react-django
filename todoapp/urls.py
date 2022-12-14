
from django.contrib import admin
from django.urls import path,include
from app.views import Todoview
from rest_framework import routers

route= routers.DefaultRouter()
route.register('',Todoview, basename="Todoview")

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include(route.urls))
]



