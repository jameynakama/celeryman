# Generated by Django 2.2.7 on 2019-12-11 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celeryman', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='github_username',
            new_name='twitter_username',
        ),
        migrations.DeleteModel(
            name='Repo',
        ),
    ]