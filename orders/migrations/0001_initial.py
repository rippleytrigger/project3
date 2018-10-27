# Generated by Django 2.1.2 on 2018-10-27 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='MenuOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Modifiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='NonSizableDishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.FloatField(default=0)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='SizableDishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price_small', models.FloatField(blank=True, default=0, null=True)),
                ('price_large', models.FloatField(blank=True, default=0, null=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Classification')),
            ],
        ),
    ]