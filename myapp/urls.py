# @author: sareeliu
# @date: 2022/3/15 12:37
from django.urls import path, re_path
from django.views.static import serve

from winSource.settings import MEDIA_ROOT
from .views import *

app_name = "myapp"
urlpatterns = [
    path('', Index.as_view()),
    path('form/', Table.as_view(), name="table"),
    path('search/', handleSearch, name="search"),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]
