from __future__ import absolute_import
from datetime import datetime, timedelta
import time

from django.utils import timezone

__all__ = ["iso_format", "before_now", "timestamp_format"]


def iso_format(date):
    return date.isoformat()[:19]


def before_now(**kwargs):
    date = datetime.utcnow() - timedelta(**kwargs)
    return date.replace(microsecond=0)


def timestamp_format(datetime):
    return time.mktime(datetime.utctimetuple()) + datetime.microsecond / 1e6


class MockClock(object):
    """Returns a distinct, increasing timestamp each time it is called."""

    def __init__(self, initial=None):
        self.time = initial or timezone.now()

    def __call__(self):
        self.time += timedelta(seconds=1)
        return self.time
