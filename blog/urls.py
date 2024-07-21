from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path("<int:post_id>/", views.post_detail, name='post_detail'),
]