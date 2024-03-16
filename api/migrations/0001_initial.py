# Generated by Django 4.2.7 on 2024-03-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(upload_to='questions')),
                ('sort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='courses')),
                ('course_duration', models.CharField(max_length=50)),
                ('level', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('type_of_course', models.CharField(choices=[('A', 'Audio'), ('I', 'Image'), ('T', 'Text')], default='T', max_length=1)),
                ('content', models.FileField(upload_to='audio/')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category')),
            ],
        ),
    ]