# coding=utf-8
from __future__ import unicode_literals

import decimal

from django.contrib.auth import authenticate, login
from django.test import TestCase
from django.utils import timezone
from mock import Mock

from .test_middleware import DummySession
from ..models import CurrentSubscription, Customer
from ..templatetags.payments_tags import change_plan_form, subscribe_form
from ..utils import get_user_model


class PaymentsTagTests(TestCase):
    def test_change_plan_form(self):
        request = Mock()
        request.META = {}
        request.session = DummySession()
        user = get_user_model().objects.create_user(username="patrick")
        user.set_password("eldarion")
        user.save()
        customer = Customer.objects.create(
            stripe_id="cus_1",
            user=user
        )
        CurrentSubscription.objects.create(
            customer=customer,
            plan="pro",
            quantity=1,
            start=timezone.now(),
            status="active",
            cancel_at_period_end=False,
            amount=decimal.Decimal("19.99")
        )
        user = authenticate(username="patrick", password="eldarion")
        login(request, user)
        context = {
            "request": request
        }
        change_plan_form(context)
        self.assertTrue("form" in context)

    def test_subscribe_form(self):
        context = {}
        subscribe_form(context)
        self.assertTrue("form" in context)
