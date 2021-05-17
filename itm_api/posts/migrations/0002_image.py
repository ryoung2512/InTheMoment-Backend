# Generated by Django 3.2.3 on 2021-05-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileurl', models.CharField(max_length=100)),
                ('datetime', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('uploaded_by', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=500)),
                ('thumbnail', models.CharField(max_length=100)),
            ],
        ),
    ]
