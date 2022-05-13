
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', include('socialmedia.urls')),
    path('delete_video/<int:video_id>', views.delete_video, name='delete_video'),
]