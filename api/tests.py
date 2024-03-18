from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, Category, Course
from django.core.files.uploadedfile import SimpleUploadedFile


class QuestionTests(TestCase):


    @classmethod 
    def setUpTestData(cls):
         
        test_question = Question.objects.create(
            question='What is your name?',
            image=SimpleUploadedFile(name='test-file.jpg', content=open('/Users/goldfur/Documents/LALI/1/1.JPG', 'rb').read(), content_type='image/jpeg'),
            sort=1
        )
        test_question.save()


    def test_question_content(self):
        question = Question.objects.get(id=1)
        q = f'{question.question}'
        image = f'{question.image}'
        sort = f'{question.sort}'

        self.assertEqual(q, 'What is your name?')
        self.assertEqual(sort, '1')
        self.assertEqual(image, 'questions/test-file.jpg')



class CategoryTests(TestCase):
    

    @classmethod
    def setUpTestData(cls):


        test_category = Category.objects.create(
            name='Math', 
            description='Math course for 4th grade', 
            image=SimpleUploadedFile(name='test-file.jpg', content=open('/Users/goldfur/Documents/LALI/1/1.JPG', 'rb').read(), content_type='image/jpeg'),
        )
        test_category.save()
            
    def test_category_content(self):
       category = Category.objects.get(id=1) 
       name = f'{category.name}'
       description = f'{category.description}'
       image = f'{category.image}'
       
       self.assertEqual(name, 'Math')
       self.assertEqual(description, 'Math course for 4th grade')
       self.assertEqual(image, 'categories/test-file.jpg')
       
