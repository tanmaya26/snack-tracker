# Generated by Django 2.2.3 on 2019-07-24 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacktracker', '0010_auto_20190724_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snacktracker.Tag'),
        ),
    ]
