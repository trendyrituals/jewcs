# Generated by Django 4.0.3 on 2022-04-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_board_of_directors_mission_our_clients_vast_network_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_of_directors',
            name='position',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
