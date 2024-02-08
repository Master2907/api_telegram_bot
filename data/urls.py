from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/datalist', DataList.as_view()),
]
