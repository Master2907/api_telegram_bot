from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/list', DataList.as_view()),
]
