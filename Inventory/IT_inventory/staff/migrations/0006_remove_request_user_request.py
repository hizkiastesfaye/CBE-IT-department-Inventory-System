# Generated by Django 4.2.2 on 2023-09-16 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_alter_request_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user_request',
        ),
    ]
