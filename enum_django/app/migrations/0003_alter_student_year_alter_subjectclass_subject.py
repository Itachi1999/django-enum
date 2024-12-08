# Generated by Django 5.1.3 on 2024-12-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('FRESHMAN', 'Freshman'), ('SOPHOMORE', 'Sophomore'), ('JUNIOR', 'Junior'), ('SENIOR', 'Senior')], default='FRESHMAN', max_length=20),
        ),
        migrations.AlterField(
            model_name='subjectclass',
            name='subject',
            field=models.CharField(choices=[('ALGO', 'Data Structures and Algorithms'), ('DL', 'Deep Learning'), ('NLP', 'Natural Language Processing'), ('TOPOLOGY', 'Algebraic Topology'), ('ALGEBRA', 'Abstract Algebra'), ('CALC', 'Multivariable Calculus'), ('LIN_ALG', 'Linear Algebra')], default='DL', max_length=50),
        ),
    ]
