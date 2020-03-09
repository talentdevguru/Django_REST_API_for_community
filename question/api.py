from .models import Answer, Question, User
from rest_framework import serializers, viewsets
from itertools import chain


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    # queryset |= Answer.objects.all()
    serializer_class = QuestionSerializer
    # def get_all_cars():
    # questions = Question.objects.filter()
    # answers = Answer.objects.filter()
    # question_list = chain(questions, answers)
    # return question_list


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
