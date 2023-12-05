# Generated by Django 5.0 on 2023-12-05 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0002_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateTimeField(null=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=30)),
                ('quality_rating', models.FloatField(default=7.0)),
                ('issue_date', models.DateTimeField(null=True)),
                ('acknowledgement_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='vendor.vendor')),
            ],
        ),
    ]
