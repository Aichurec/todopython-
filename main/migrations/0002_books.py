# Generated by Django 3.1.7 on 2021-04-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
