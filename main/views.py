from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Language, Quiz, Question, Participant, Answer, Result
from .serializers import (LanguageViewSerializer, QuizViewSerializer, QuestionViewSerializer,
                          ParticipantSerializer, AnswerViewSerializer, ResultViewSerializer)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageViewSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(LanguageView, self).get_permissions()


class QuizView(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizViewSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'POST', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(QuizView, self).get_permissions()


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionViewSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'POST', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(QuestionView, self).get_permissions()


class ParticipantView(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerViewSerializer


class ResultView(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultViewSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'POST', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(ResultView, self).get_permissions()

