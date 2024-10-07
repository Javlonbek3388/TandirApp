from rest_framework.routers import DefaultRouter
from .views import (LanguageView, QuizView, QuestionView,
                    ParticipantView, AnswerView, ResultView)

router = DefaultRouter()
router.register(r'quizzes', QuizView)
router.register(r'questions', QuestionView)
router.register(r'participant', ParticipantView)
router.register(r'answers', AnswerView)
router.register(r'results', ResultView)
router.register(r'language', LanguageView)

urlpatterns = router.urls