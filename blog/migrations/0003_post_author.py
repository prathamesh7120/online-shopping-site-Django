# Generated by Django 4.0.1 on 2022-02-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author_remove_post_blogimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]