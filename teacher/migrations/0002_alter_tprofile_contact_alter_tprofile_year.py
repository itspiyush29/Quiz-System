# Generated by Django 4.1 on 2022-11-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tprofile',
            name='year',
            field=models.CharField(max_length=5),
        ),
    ]
