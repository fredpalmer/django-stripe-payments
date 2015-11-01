# coding=utf-8
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.generic import View


class MockView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
