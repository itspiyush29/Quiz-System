# Generated by Django 4.1 on 2022-11-21 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizze_lb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizze',
            name='lb',
        ),
    ]
