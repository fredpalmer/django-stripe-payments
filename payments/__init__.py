# coding=utf-8
from __future__ import unicode_literals

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("django-stripe-payments").version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"
