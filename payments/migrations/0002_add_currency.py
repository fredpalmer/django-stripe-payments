# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField("charge", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField("currentsubscription", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField("invoice", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField("invoiceitem", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField("transfer", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField("transferchargefee", "currency", models.CharField(default='usd', max_length=10)),
        migrations.AddField(
            model_name='charge',
            name='captured',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='charge',
            name='amount',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='charge',
            name='amount_refunded',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='charge',
            name='fee',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='amount',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='canceled_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='current_period_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='current_period_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='ended_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='trial_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentsubscription',
            name='trial_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='livemode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subtotal',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='amount',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='proration',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='adjustment_fees',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='adjustment_gross',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='charge_fees',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='collected_fee_gross',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='refund_fees',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='refund_gross',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='validation_fees',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transferchargefee',
            name='amount',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
    ]
