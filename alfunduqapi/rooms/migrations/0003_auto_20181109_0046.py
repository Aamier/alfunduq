# Generated by Django 2.1.2 on 2018-11-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20181109_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='number',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
