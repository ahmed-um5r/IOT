# Generated by Django 4.1.7 on 2023-02-26 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_confirm', '0019_post1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
