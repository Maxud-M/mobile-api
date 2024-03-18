# Generated by Django 4.2.7 on 2024-03-18 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_course_type_of_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='sort',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]