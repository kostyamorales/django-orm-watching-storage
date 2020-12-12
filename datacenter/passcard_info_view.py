from datacenter.models import Passcard, Visit, get_duration, is_visit_long, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        flag = is_visit_long(visit)
        this_passcard_visits.append({
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": flag
        })
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
