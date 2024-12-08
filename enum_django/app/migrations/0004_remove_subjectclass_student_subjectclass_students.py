# Generated by Django 5.1.3 on 2024-12-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_student_year_alter_subjectclass_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectclass',
            name='student',
        ),
        migrations.AddField(
            model_name='subjectclass',
            name='students',
            field=models.ManyToManyField(related_name='students', to='app.student'),
        ),
    ]