# Generated by Django 4.0.1 on 2022-01-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_video_unique_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='unique_key',
            field=models.CharField(default='0000000', editable=False, max_length=7),
        ),
    ]
