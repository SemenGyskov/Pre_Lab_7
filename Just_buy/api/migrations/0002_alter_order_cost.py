# Generated by Django 4.1.7 on 2023-03-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая Стоимость Заказа'),
        ),
    ]
