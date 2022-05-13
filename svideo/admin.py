from django.contrib import admin
from django.forms import Field

# Register your models here.
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'video_file', 'timestamp', 'updated']

