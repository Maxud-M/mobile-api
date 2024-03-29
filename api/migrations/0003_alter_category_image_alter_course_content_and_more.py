# Generated by Django 4.2.7 on 2024-03-18 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_offlineorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.FileField(upload_to='courses/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/'),
        ),
        migrations.AlterField(
            model_name='offlineorder',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^(8|\\+7)\\s*[\\-]?\\s*((\\(\\d{3}\\)\\s*[\\-]?\\s*\\d{3}\\s*[\\-]\\s*\\d{2}\\s*[\\-]?\\s*\\d{2})|(\\s*\\d{3}\\s*[\\-]?\\s*\\d{3}\\s*[\\-]?\\s*\\d{2}\\s*[\\-]?\\s*\\d{2}\\s*))$')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='questions/'),
        ),
    ]
