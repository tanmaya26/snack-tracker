# Generated by Django 2.2.3 on 2019-07-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacktracker', '0011_auto_20190724_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='snack_tag',
            field=models.CharField(default='SWEET', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='snack',
            name='snack_image',
            field=models.CharField(default='image', max_length=200, null=True),
        ),
    ]
