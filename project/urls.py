from django.contrib import admin
from django.urls import path
from app.views import inicio, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio_url"),
    path('sobre',sobre,name="sobre_url")
]