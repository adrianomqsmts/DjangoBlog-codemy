# Generated by Django 3.1.4 on 2021-01-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
