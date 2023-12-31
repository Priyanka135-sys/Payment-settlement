# Generated by Django 4.1.11 on 2023-10-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0003_alter_new_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_payment',
            name='recipient_id',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='settled_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
