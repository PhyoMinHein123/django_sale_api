# Generated by Django 3.2.23 on 2024-03-02 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descripton',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='descripton',
            new_name='description',
        ),
    ]