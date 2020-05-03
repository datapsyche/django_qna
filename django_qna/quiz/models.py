from django.db import models

# Create your models here.

class Quiz(models.Model):
    quiz_description = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.quiz_description}"

class Question(models.Model):
    question_text = models.TextField()
    created = models.DateTimeField()
    quiz = models.ForeignKey(to = Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    choice_text = models.TextField()
    question = models.ForeignKey(to = Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.choice_text}"

class Answer(models.Model):
    question = models.ForeignKey(to = Question, on_delete = models.DO_NOTHING)
    correct_choice = models.ForeignKey(to = Choice, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.question.question_text}:-:{self.correct_choice.choice_text}"


