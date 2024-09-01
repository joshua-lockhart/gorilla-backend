from rest_framework import viewsets
from .models import WebPage, Question, Answer
from .serializers import WebPageSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class WebPageViewSet(viewsets.ModelViewSet):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        webpage = self.get_object()
        questions = Question.objects.filter(web_page=webpage)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    