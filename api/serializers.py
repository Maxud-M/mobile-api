from rest_framework import serializers
from .models import Question, Course, Category, OfflineOrder


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question', 'image')
        model = Question


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'image')
        model = Category
        

class CourseSerializer(serializers.ModelSerializer):

    category_description = serializers.CharField(source='category_id.description', read_only=True)

    class Meta:
        fields = ('id', 'name', 'image', 'course_duration', 'category_description', 'level', 'type_of_course', 'content')
        model = Course

    def get_fields(self):
        fields = super().get_fields()
        print(fields)
        exclude_fields = self.context.get('exclude_fields', [])
        for field in exclude_fields:
            fields.pop(field, default=None)
        
        return fields


class OfflineOrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'phone_number')
        model = OfflineOrder