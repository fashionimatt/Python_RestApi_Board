from django.urls import path, include
from .views import notice_view

urlpatterns = [
    path('notice/', notice_view.Notice.as_view(), name='notice'),
    path('notice/detail', notice_view.Notice_Detail.as_view(), name='notice_detail'),
    path('notice/write', notice_view.Notice_Write.as_view(), name='notice_write'),
    path('notice/writeAction', notice_view.Notice_Write_Action.as_view(), name='notice_write_action'),
]
