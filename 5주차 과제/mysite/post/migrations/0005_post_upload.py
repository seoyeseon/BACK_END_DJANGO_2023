# Generated by Django 4.2.1 on 2023-05-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
