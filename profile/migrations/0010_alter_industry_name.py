# Generated by Django 4.1.5 on 2023-01-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_alter_profile_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
