# Generated by Django 2.2.4 on 2020-05-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='priv',
            field=models.CharField(default='Moderator', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
