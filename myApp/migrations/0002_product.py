# Generated by Django 4.2.11 on 2024-11-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
