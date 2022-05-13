from turtle import title
from urllib import response
from django.shortcuts import render
from .models import Video
import os


# Create your views here.
def index(request):
    video = Video.objects.all()
    return render(request, 'index.html', {'video': video})

def delete_video(request, video_id: int):
    video = Video.objects.filter(id=video_id).first()
    if not video:
        return response({'error': 'Video not found'}, status=404)

    else:
        getfilelocation = video.video_file
        try:
            os.remove(getfilelocation.path) #remove file frm static folder
            video.delete() #delete frm db
            return render(request, 'index.html')
        except:
            video.delete() #delete frm db
            raise Exception('Video not found')

            # getfilelocation = video.video_file
            # os.path.exists(getfilelocation.path)

