# Generated by Django 4.1 on 2022-09-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
