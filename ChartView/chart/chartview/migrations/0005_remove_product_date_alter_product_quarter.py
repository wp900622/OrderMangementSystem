# Generated by Django 5.0.2 on 2024-02-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartview', '0004_rename_category_product_quarter_alter_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.AlterField(
            model_name='product',
            name='quarter',
            field=models.CharField(default='', max_length=20, null=True, unique=True),
        ),
    ]
