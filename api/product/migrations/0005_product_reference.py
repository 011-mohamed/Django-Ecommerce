# Generated by Django 4.0.4 on 2022-06-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
