# Generated by Django 5.0.6 on 2024-05-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=200)),
                ('fees', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('confirm_password', models.CharField(max_length=200)),
            ],
        ),
    ]
