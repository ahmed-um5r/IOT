# Generated by Django 4.1.7 on 2023-02-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_confirm', '0018_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
