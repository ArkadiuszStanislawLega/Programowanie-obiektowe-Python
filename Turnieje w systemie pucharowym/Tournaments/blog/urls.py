from django.urls import path
from blog.views import *

urlpatterns = [
    path('', AllPostsView.as_view(), name="blog-home"),


]
