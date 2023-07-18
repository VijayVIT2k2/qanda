from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='questions')
    objects = models.Manager()
    # def __str__(self) -> str:
    #     return title
    
class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='answers')
    objects = models.Manager()
