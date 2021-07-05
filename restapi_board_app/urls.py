from django.urls import path, include
from .views.notice_view import Notice

urlpatterns = [
    path('notice/', Notice.as_view(), name='notice')
]
