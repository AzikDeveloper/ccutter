# Generated by Django 4.0 on 2021-12-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='color',
            field=models.CharField(blank=True, choices=[('green', 'Green'), ('blue', 'Blue'), ('white', 'White'), ('red', 'Red')], default='white', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(blank=True, choices=[('green', 'Green'), ('blue', 'Blue'), ('white', 'White'), ('red', 'Red')], default='green', max_length=16, null=True),
        ),
    ]
