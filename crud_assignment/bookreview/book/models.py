from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    Score_Choices = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    )
    title = models.CharField(max_length=200)
    review = models.TextField()
    price = models.FloatField()
    score = models.CharField(max_length=1, choices=Score_Choices)
    picture = models.FileField(null=True, blank=True, default='static/error.jpg')
    author = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.CharField(max_length=50, default="")