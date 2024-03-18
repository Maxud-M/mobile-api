from django.urls import path
from .views import QuestionList, CourseList, CourseDetail


urlpatterns = [
    path('questions/', QuestionList.as_view()),
    path('courses/', CourseList.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),
] 

