from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Language, Quiz, Question, Participant, Answer, Result
from .serializers import (LanguageViewSerializer, QuizViewSerializer, QuestionViewSerializer,
                          ParticipantSerializer, AnswerViewSerializer, ResultViewSerializer)


class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageViewSerializer


class QuizView(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizViewSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionViewSerializer


class ParticipantView(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerViewSerializer


class ResultView(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultViewSerializer

