# Generated by Django 2.1.2 on 2018-12-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonsizabledishes',
            name='topping_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sizabledishes',
            name='topping_number',
            field=models.IntegerField(default=0),
        ),
    ]