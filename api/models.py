from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Question(models.Model):

    question = models.TextField()
    image = models.ImageField(upload_to='questions/')
    sort = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)]) 

    
    def __str__(self):
        return self.question

    
class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name 


class Course(models.Model):

    class LevelChoices(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'
    
    AUDIO = 'AUDIO'
    VIDEO = 'VIDEO'
    TEXT = 'TEXT'

    TYPE_CHOICES = [
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
        (TEXT, 'Text'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/')
    course_duration = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    level = models.IntegerField(choices=LevelChoices.choices, default=LevelChoices.LOW,)
    type_of_course = models.CharField(max_length=5, choices=TYPE_CHOICES, default=TEXT)
    content = models.FileField(upload_to='courses/')


    def __str__(self):
        return self.name


class OfflineOrder(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12, validators=[
        RegexValidator(r"^(8|\+7)\s*[\-]?\s*((\(\d{3}\)\s*[\-]?\s*\d{3}\s*[\-]\s*\d{2}\s*[\-]?\s*\d{2})|(\s*\d{3}\s*[\-]?\s*\d{3}\s*[\-]?\s*\d{2}\s*[\-]?\s*\d{2}\s*))$")])

    def __str__(self):
        return self.name
