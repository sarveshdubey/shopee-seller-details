# Generated by Django 4.1.3 on 2022-11-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetLinks_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]