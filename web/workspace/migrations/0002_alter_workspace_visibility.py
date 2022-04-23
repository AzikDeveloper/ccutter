# Generated by Django 4.0 on 2021-12-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('blocked', 'Blocked')], default='private', max_length=64, null=True),
        ),
    ]
