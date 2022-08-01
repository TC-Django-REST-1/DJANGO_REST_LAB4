# Generated by Django 4.0.6 on 2022-08-01 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('established_at', models.DateField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]
