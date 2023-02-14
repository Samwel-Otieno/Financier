from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Create_blogs(models.Model):
    owner=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    article=models.TextField()
    image=models.ImageField(blank=True, null=True, upload_to='media/')
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def description(self):
        return self.article[:20]+ '...'

class Comment(models.Model):
    blog=models.ForeignKey(Create_blogs, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    comment=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment