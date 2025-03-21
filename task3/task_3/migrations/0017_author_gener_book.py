# Generated by Django 5.0 on 2025-03-16 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0016_remove_profile2model_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gener', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('Publish_date', models.DateField()),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Book/')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_3.author')),
                ('Gener', models.ManyToManyField(to='task_3.gener')),
            ],
        ),
    ]
