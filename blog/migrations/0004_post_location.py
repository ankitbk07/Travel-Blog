# Generated by Django 4.1.5 on 2023-08-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
