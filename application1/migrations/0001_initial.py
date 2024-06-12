# Generated by Django 5.0.6 on 2024-06-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('education', models.CharField(max_length=500)),
                ('accomplishments', models.CharField(max_length=1000)),
                ('work_experence', models.CharField(max_length=1000)),
                ('certifications', models.CharField(max_length=1000)),
            ],
        ),
    ]
