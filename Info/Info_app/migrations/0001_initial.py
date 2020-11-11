# Generated by Django 3.1.2 on 2020-11-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('courses', models.CharField(max_length=1)),
                ('category', models.CharField(max_length=1)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
    ]