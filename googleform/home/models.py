from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .choices import Question_Choices
from .utils.utility import generate_random_string

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Choices(BaseModel):
    choice = models.CharField(max_length=100)
    

class Question(BaseModel):
    question = models.CharField(max_length=100)
    question_type = models.CharField(choices = Question_Choices, max_length=100)
    required = models.BooleanField(default = False)
    choices = models.ManyToManyField(Choices, related_name = "questions_choices",blank = True)

class Form(BaseModel):
    code = models.CharField(max_length=100,unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User,on_delete = models.CASCADE)
    background_color = models.CharField(max_length=100, default = "#272124")
    collect_email = models.BooleanField(default = False)
    questions = models.ManyToManyField(Question, related_name = "questions")

    @staticmethod
    def create_blank_form(user):
        form_token = generate_random_string()
        choices = Choices.objects.create(choice = "option 1")
        question = Question.objects.create(question_type = 'Multiple Choice',question = "Untitled Question")
        question.choices.add(choices)
        form = Form(code= form_token, title ="Untitled Form",creator = user)
        form.save()
        form.questions.add(question)
        return form


class Answers(BaseModel):
    answer = models.CharField(max_length=100)
    answer_to = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = "answer_to")
class Response(BaseModel):
    response_code = models.CharField(max_length=100,unique=True)
    response_to = models.ForeignKey(Form, on_delete = models.CASCADE)
    responder_ip = models.CharField(max_length=100)
    responder_email = models.EmailField(null = True, blank = True)
    response = models.ManyToManyField(Answers, related_name = "answers")