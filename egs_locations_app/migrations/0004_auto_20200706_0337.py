# Generated by Django 3.0.3 on 2020-07-06 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egs_locations_app', '0003_poi_countpurplecontainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playfield',
            name='size',
            field=models.ForeignKey(blank=True, default=None, help_text='Size of the playfield or NULL if orbit', null=True, on_delete=django.db.models.deletion.CASCADE, to='egs_locations_app.PlayfieldSize'),
        ),
    ]
