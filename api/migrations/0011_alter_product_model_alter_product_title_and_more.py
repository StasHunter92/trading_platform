# Generated by Django 4.2.1 on 2023-06-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_supplier_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
