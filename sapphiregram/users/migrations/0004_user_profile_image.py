# Generated by Django 2.0.7 on 2018-07-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180724_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
