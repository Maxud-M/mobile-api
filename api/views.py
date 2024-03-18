from rest_framework import generics
from rest_framework.response import Response
from .models import Question, Course
from .serializers import QuestionSerializer, CourseSerializer 



class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()#.order_by('level').order_by('type_of_course')
    serializer_class = CourseSerializer

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
    

