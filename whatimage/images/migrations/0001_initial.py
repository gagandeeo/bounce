# Generated by Django 3.0.7 on 2020-06-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('classfied', models.CharField(blank=True, max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
