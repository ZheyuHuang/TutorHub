# Generated by Django 2.2.5 on 2020-01-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('is_admin', models.IntegerField(default=0)),
                ('is_publisher', models.IntegerField(default=0)),
                ('preference', models.TextField()),
            ],
        ),
    ]