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
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        self.entered_at = timezone.localtime(self.entered_at)
        if self.leaved_at is None:
            self.now = timezone.localtime()
            self.duration = datetime.timedelta.total_seconds(self.now - self.entered_at)
            return self.duration
        self.leaved_at = timezone.localtime(self.leaved_at)
        self.duration = datetime.timedelta.total_seconds(self.leaved_at - self.entered_at)
        return self.duration

    def format_duration(self, seconds):
        self.hours = int(seconds // 3600)
        self.minutes = int((seconds % 3600) // 60)
        self.duration = f'{self.hours}ч {self.minutes}мин'
        return self.duration

    def is_visit_long(self, minutes=60):
        self.duration = self.get_duration()
        self.minutes = self.duration // 60
        if self.minutes > minutes:
            return True
        return False

