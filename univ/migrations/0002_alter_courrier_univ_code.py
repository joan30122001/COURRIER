# Generated by Django 4.1.4 on 2023-07-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courrier_univ',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
