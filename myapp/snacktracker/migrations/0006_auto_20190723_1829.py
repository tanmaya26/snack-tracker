# Generated by Django 2.2.3 on 2019-07-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacktracker', '0005_auto_20190723_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='likes',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requests',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
