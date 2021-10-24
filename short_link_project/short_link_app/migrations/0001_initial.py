# Generated by Django 3.2.8 on 2021-10-24 13:23

from django.db import migrations, models
import short_link_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLinkCreator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField()),
                ('shorted_url', models.URLField(blank=True, max_length=15, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('expiration_time', models.DateTimeField(
                    default=short_link_app.models.shortener_links_utils.expire_at)),
                ('times_redirected', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]