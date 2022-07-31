# Generated by Django 4.0.6 on 2022-07-31 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='established_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
