# Generated by Django 3.2.3 on 2021-05-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
