# Generated by Django 4.2.7 on 2025-03-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0003_profilemodel_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='City',
        ),
        migrations.AddField(
            model_name='profile2model',
            name='City',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
