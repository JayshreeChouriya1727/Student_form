# Generated by Django 3.1.2 on 2020-11-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_app', '0002_auto_20201109_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='desc',
            field=models.TextField(max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=120),
        ),
    ]
