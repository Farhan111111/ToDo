# Generated by Django 3.2.12 on 2022-03-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-06-27'),
            preserve_default=False,
        ),
    ]