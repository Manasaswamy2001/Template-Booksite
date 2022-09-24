# Generated by Django 4.1 on 2022-09-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('published_year', models.DateField()),
                ('averagerating', models.FloatField()),
            ],
        ),
    ]
