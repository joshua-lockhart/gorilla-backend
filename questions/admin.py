from django.contrib import admin
from .models import WebPage, Question, Answer

admin.site.register(WebPage)
admin.site.register(Question)
admin.site.register(Answer)