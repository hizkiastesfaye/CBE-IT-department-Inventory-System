# Generated by Django 4.2.2 on 2023-09-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_request_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
