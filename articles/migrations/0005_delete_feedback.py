# Generated by Django 4.1.6 on 2023-07-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_feedback_title_remove_feedback_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]