from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/images',blank=True,null=True)

    class Meta :
        app_label = 'posts'
    def __str__(self) :
        return self.title