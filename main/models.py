from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import User


class Language(models.Model):
    lan_name = models.CharField(max_length=55, blank=True, null=True)
    icon = models.ImageField(upload_to='icon/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(blank=True, null=True)
    time_limit = models.IntegerField(default=12)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{User.username} - {self.quiz.name}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"


class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
