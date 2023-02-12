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

    def desctription(self):
        return self.article[20+ '...']