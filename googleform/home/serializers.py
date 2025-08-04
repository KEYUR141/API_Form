from rest_framework import serializers
from .models import (
    Form, Answers, Response, Question, Choices
)



class FormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ['created_at','updated_at']
    
    def to_representation(self, instance):
        questions = instance.questions.all()
        question_serializers = QuestionSerializers(questions, many = True)
        payload = {
            'form': instance.id,
            'code': instance.code,
            'title': instance.title,
            'description': instance.description,
            'creator':instance.creator.username,
            'background_color': instance.background_color,
            'questions': question_serializers.data
        }

        return payload
class AnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        exclude = ['created_at','updated_at']

class ResponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Response
        exclude = ['created_at','updated_at']

class QuestionSerializers(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    class Meta:
        model = Question
        exclude = ['created_at','updated_at']
    
    def get_choices(self, object):
        return "This is a method "


class ChoicesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Choices
        exclude = ['created_at','updated_at']

    