from rest_framework import generics
from rest_framework.response import Response
from .models import Question, Course, OfflineOrder
from .serializers import QuestionSerializer, CourseSerializer, OfflineOrderSerializer
from django_filters.rest_framework import DjangoFilterBackend


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()#.order_by('level').order_by('type_of_course')
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['level', 'type_of_course']


class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['exclude_fields'] = [
                'course_duration',
                'id',
                'level',
                'type_of_course'
        ]
        
        return context
    

class OffOrderList(generics.ListCreateAPIView):
    queryset = OfflineOrder.objects.all()
    serializer_class = OfflineOrderSerializer 