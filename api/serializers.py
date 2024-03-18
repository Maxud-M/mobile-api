from rest_framework import serializers
from .models import Question, Course, Category 

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
    
   # def __init__(self, *args, **kwargs):
   #     remove_fields = kwargs.pop('remove_fields', None)
   #     super(CourseSerializer , self).__init__(*args, **kwargs)

   #     if remove_fields is not None:
   #         exlude_fields = set(remove_fields)
   #         for field_name in exlude_fields:
   #             self.fields.pop(field_name)
