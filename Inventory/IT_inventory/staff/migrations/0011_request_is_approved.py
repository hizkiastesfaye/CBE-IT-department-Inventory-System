# Generated by Django 4.2.2 on 2023-09-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_staffdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]