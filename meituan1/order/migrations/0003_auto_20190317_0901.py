# Generated by Django 2.1.7 on 2019-03-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_customer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.IntegerField(default=0),
        ),
    ]
