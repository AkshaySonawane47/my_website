# Generated by Django 4.1.5 on 2023-03-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_remove_invoice_level_invoice_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='mobile',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
