# Generated by Django 4.1.4 on 2023-06-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_universite'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Chef_univ',
            field=models.BooleanField(default=False, verbose_name='Is Chef Universite'),
        ),
    ]
