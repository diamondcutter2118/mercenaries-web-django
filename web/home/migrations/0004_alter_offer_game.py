# Generated by Django 4.0 on 2022-02-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='game',
            field=models.CharField(max_length=30),
        ),
    ]
