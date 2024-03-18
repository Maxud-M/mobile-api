import os
from django.contrib import admin
from .models import Question, Category, Course, OfflineOrder
import shutil
from django.conf import settings

class CourseAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)


        base_dir = str(settings.BASE_DIR)
        image_path = base_dir + obj.image.url # /media/courses/image.* -> courses/obj.id/image.*
        content_path = base_dir + obj.content.url  # /media/courses/content.* -> courses/obj.id/content/content.* 

        new_image_path = obj.image.url[:15] + str(obj.id) + obj.image.url[14:]
        new_content_path = obj.content.url[:15] + str(obj.id) + '/content' + obj.content.url[14:]


        obj.image = new_image_path[7:]
        obj.content = new_content_path[7:]
        obj.save(update_fields=['image', 'content'])
       
        os.makedirs(base_dir + os.path.dirname(new_image_path), exist_ok=True)
        os.makedirs(base_dir + os.path.dirname(new_content_path), exist_ok=True)
        shutil.move(image_path, base_dir + new_image_path)
        shutil.move(content_path, base_dir + new_content_path)

         


admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(OfflineOrder)
