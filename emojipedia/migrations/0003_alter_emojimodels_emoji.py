# Generated by Django 4.1.1 on 2022-12-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emojipedia', '0002_alter_emojimodels_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emojimodels',
            name='emoji',
            field=models.CharField(max_length=10),
        ),
    ]
