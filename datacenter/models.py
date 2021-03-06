from django.db import models
import datetime
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        entered_at = timezone.localtime(self.entered_at)
        end_time = timezone.localtime(self.leaved_at)
        if self.leaved_at is None:
            end_time = timezone.localtime()
        seconds = datetime.timedelta.total_seconds(end_time - entered_at)
        return seconds

    def is_visit_long(self, mins=60):
        seconds = self.get_duration()
        minutes = seconds // 60
        return minutes > mins


def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    duration = f'{hours}ч {minutes}мин'
    return duration
