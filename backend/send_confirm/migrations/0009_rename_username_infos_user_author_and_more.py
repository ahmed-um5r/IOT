# Generated by Django 4.1.5 on 2023-01-13 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_confirm', '0008_alter_infos_user_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infos_user',
            old_name='username',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='infos_user',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
