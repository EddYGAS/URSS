# Generated by Django 4.0.1 on 2023-01-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
