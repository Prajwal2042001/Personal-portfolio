# Generated by Django 4.2.5 on 2023-09-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('abstract', models.CharField(max_length=10000)),
                ('skills', models.CharField(max_length=500)),
                ('slno', models.IntegerField()),
            ],
        ),
    ]