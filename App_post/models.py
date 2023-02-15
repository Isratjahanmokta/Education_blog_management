from django.db import models
from Auth.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images', blank=True)
    caption = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-created',]

    

# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class Like(models.Model):
    liked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name= 'likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'likes')

class Comment(models.Model):
    commented_by = models.ForeignKey(CustomUser, related_name='user_on_comment', on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment_on_post', on_delete = models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to = 'comment_images', null=True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('-created',)