# Generated by Django 3.2.3 on 2021-06-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cst', models.CharField(default='', max_length=20)),
                ('prd', models.CharField(default='', max_length=30)),
            ],
        ),
    ]