# Generated by Django 3.2.8 on 2021-11-01 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_user_secret_key_userotpcode_secret_key'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSecretKey',
        ),
    ]