# Generated by Django 3.1.7 on 2021-04-18 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210412_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='books',
            name='year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]