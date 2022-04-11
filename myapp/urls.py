# @author: sareeliu
# @date: 2022/3/15 12:37
from django.urls import path, re_path
from django.views.static import serve

from winSource.settings import MEDIA_ROOT
from .views import *

app_name = "myapp"
urlpatterns = [
    path('', Index.as_view()),
    path('table/', Table.as_view(), name="table"),
    path('upload_and_quote/', UploadAndQuote.as_view(), name="upload_and_quote"),
    path('about_us/', AboutUs.as_view(), name="aboutus"),
    path('search/', handleSearch, name="search"),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]
