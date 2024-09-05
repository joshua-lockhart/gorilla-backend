from django.db import models
from django.contrib.auth.models import User

class WebPage(models.Model):
    dokuwiki_id = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.TextField()
    web_page = models.ForeignKey(WebPage, related_name='questions', on_delete=models.CASCADE)
    matchText = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text