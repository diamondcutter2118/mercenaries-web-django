# Generated by Django 4.0 on 2022-02-15 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_offer_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_name', to='home.game'),
        ),
    ]
