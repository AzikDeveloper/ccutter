# Generated by Django 4.0 on 2021-12-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_board_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('blocked', 'Blocked')], default='private', max_length=64, null=True),
        ),
    ]
