# Generated by Django 3.0.6 on 2020-08-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_dete',
            new_name='create_date',
        ),
    ]