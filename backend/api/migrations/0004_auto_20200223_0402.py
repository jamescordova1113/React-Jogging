# Generated by Django 3.0.3 on 2020-02-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200218_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]