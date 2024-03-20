import os
from django.contrib import admin
from django.http import HttpRequest
from .models import Question, Category, Course, OfflineOrder
import shutil
from django.conf import settings


class CourseAdmin(admin.ModelAdmin):
    

    def delete_model(self, request: HttpRequest, obj) -> None:
        id = obj.id

        base_dir = str(settings.BASE_DIR)
        delete_path = base_dir + f'/media/courses/{id}'
        shutil.rmtree(delete_path)

        return super().delete_model(request, obj)

    
    def change_file(self, old_file: str, new_file: str) -> str:
        base_dir = str(settings.BASE_DIR)

        # Name of dir where we should place new file and delete old file from 
        dir_name = os.path.dirname(old_file)
        # Basename of new file 
        file_name = os.path.basename(new_file)

        # Moving new file to the right place
        new_path = base_dir + dir_name + '/' + file_name
        old_path = base_dir + new_file
        shutil.move(old_path, new_path)
        
        # Delete old file
        os.remove(base_dir + old_file)
        return dir_name + '/' + file_name


    def create_files(self, obj):
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

    



    def save_model(self, request, obj, form, change):
        if change: 
            old_course = Course.objects.get(id=obj.id)
            super().save_model(request, obj, form, change)
            if old_course.image.url != obj.image.url:
                new_image_path = self.change_file(old_course.image.url, obj.image.url)
                obj.image = new_image_path
                obj.save(update_fields=['image'])
            if old_course.content.url != obj.content.url:
                new_content_path = self.change_file(old_course.content.url, obj.content.url)
                obj.content = new_content_path
                obj.save(update_fields=['content'])
        
        else:
            super().save_model(request, obj, form, change)
            self.create_files(obj)



admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(OfflineOrder)
