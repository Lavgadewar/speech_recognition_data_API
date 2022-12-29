
# from django.contrib import admin
from django.urls import path
from data_api.views import DataList

urlpatterns = [
    path('list/', DataList.as_view( ))
]
