# Generated by Django 5.1.3 on 2024-12-02 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='John Doe', max_length=200)),
                ('year', models.CharField(choices=[('FRESHMAN', 1), ('SOPHOMORE', 2), ('JUNIOR', 3), ('SENIOR', 4)], default=1, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('domain', models.CharField(choices=[('CS', 'ComputerScience'), ('MTH', 'Mathematics')], default='ComputerScience', max_length=30)),
                ('subject', models.CharField(choices=[('ALGO', 'Data Structures and Algorithms'), ('DL', 'Deep Learning'), ('NLP', 'Natural Language Processing'), ('TOPOLOGY', 'Algebraic Topology'), ('ALGEBRA', 'Abstract Algebra'), ('CALC', 'Multivariable Calculus'), ('LIN_ALG', 'Linear Algebra')], default='Deep Learning', max_length=50)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='app.student')),
            ],
        ),
    ]