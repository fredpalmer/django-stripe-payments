# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_add_currency'),
    ]

    operations = [
        migrations.RenameModel("CurrentSubscription", "Subscription"),
        migrations.AlterField(
            model_name='subscription',
            name='customer',
            field=models.ForeignKey(to='payments.Customer', null=True),
        ),
    ]
