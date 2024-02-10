# Generated by Django 5.0 on 2024-01-19 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_albums_model_delete_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums_model',
            name='album_rating',
            field=models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], max_length=10),
        ),
    ]