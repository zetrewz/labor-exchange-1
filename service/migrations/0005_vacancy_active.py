# Generated by Django 5.0 on 2023-12-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_resume_about_remove_resume_citizenship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
