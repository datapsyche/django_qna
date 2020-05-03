from django.contrib import admin
from django.urls import path, include
from .views import index, show_questions, show_choices

from rest_framework import routers
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, AnswerViewSet


router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'answer', AnswerViewSet)

urlpatterns = [
    path('', index, name="index" ),
    path('', include(router.urls)),
    path('<int:quiz_id>/', show_questions, name="show_questions"),
    path('questions/<int:question_id>/', show_choices, name="show_choices")
]
