# Generated by Django 4.0 on 2022-02-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_game_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='game',
            field=models.CharField(max_length=30),
        ),
    ]