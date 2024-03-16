from django.contrib import admin
from .models import Question, Category, Course, OfflineOrder

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(OfflineOrder)
