# Generated by Django 4.1.1 on 2024-03-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0020_saleorder_salesorderreference_salesorderitems_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorder',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
