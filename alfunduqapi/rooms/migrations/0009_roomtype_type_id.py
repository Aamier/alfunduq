# Generated by Django 2.1.2 on 2018-11-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20181111_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='type_id',
            field=models.CharField(default=1, max_length=10, unique=True),
        ),
    ]
