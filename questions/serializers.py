from rest_framework import serializers
from .models import WebPage, Question, Answer

class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'