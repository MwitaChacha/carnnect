# Generated by Django 3.2.9 on 2022-01-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_rename_cc_sale_engine_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='shop',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
