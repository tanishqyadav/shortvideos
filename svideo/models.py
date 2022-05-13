from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=1000)
    video_file = models.FileField(upload_to='videos/%y')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

# class votes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE, primary_key=True)
#     vote = models.Choices(choices=((0, 'Like'), (1, 'Dislike')))

#     def __str__(self):
#         return self.vote 