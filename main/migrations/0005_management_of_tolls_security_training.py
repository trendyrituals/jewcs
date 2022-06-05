# Generated by Django 4.0.3 on 2022-03-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_info_feathers_to_our_cap_welfare_measures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management_of_tolls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('first_detail', models.TextField()),
                ('second_detail', models.TextField(blank=True)),
                ('third_detail', models.TextField(blank=True)),
                ('fourth_detail', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Security_training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]