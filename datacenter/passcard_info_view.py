from datacenter.models import Passcard, Visit, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        seconds = visit.get_duration()
        flag = visit.is_visit_long()
        this_passcard_visits.append({
            "entered_at": visit.entered_at,
            "duration": format_duration(seconds),
            "is_strange": flag
        })
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
