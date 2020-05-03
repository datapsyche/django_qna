from django.shortcuts import render
from rest_framework import viewsets
from .models import Quiz, Question, Choice, Answer
from .serializer import QuizSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer

# Create your views here.

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

def index(request):
    all_quiz = Quiz.objects.all()
    return render(request=request, template_name='quiz/index.html', context = { 'all_quiz': all_quiz})

def show_questions(request, quiz_id):
    all_questions = Question.objects.filter(quiz_id=quiz_id)    
    return render(request=request, template_name='quiz/questions.html', context = { 'all_questions': all_questions})

def show_choices(request, question_id):
    all_choices = Choice.objects.all()
    relevant_choices = [choice for choice in all_choices if choice.question.id == question_id]
    return render(request=request, template_name='quiz/choices.html', context = { 'all_choices': relevant_choices})





