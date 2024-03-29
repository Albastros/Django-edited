# Generated by Django 5.0.1 on 2024-03-03 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelOfEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100, verbose_name='Level of Education')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='level_of_education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.levelofeducation', verbose_name='Level of Education'),
        ),
    ]
