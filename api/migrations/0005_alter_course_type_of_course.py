# Generated by Django 4.2.7 on 2024-03-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_course_type_of_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type_of_course',
            field=models.CharField(choices=[('AUDIO', 'Audio'), ('VIDEO', 'Video'), ('TEXT', 'Text')], default='TEXT', max_length=5),
        ),
    ]
