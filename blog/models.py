from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):

    status_choices=[
        ('d', 'Draft'), 
        ('p', 'Published'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=3,null=True,blank=True)
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices,max_length=3)

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(User,models.CASCADE)
    time_stamp = models.DateField(auto_now=True)
    content = models.TextField()
    blog = models.ForeignKey(Blog,related_name='comment',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.blog}"


class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='like',on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.blog}"


class PostView(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_views = models.BooleanField( default=False)
    blog = models.ForeignKey(Blog, related_name='view_count', on_delete=models.CASCADE)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.blog}"



