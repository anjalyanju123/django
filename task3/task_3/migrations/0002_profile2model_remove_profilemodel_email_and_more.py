# Generated by Django 5.0 on 2025-03-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=40)),
                ('Phone', models.IntegerField()),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='Email',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='Age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Name',
            field=models.CharField(max_length=20),
        ),
    ]
