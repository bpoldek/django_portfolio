# Generated by Django 4.1 on 2022-09-01 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author_remove_post_text_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=datetime.date.today()),
            preserve_default=False,
        ),
    ]
