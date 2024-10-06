from rest_framework import serializers
from .models import Language, Quiz, Question, Participant, Answer, Result


class LanguageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class QuizViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class AnswerViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ResultViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
