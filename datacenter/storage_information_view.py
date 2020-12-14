from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved_visits:
        duration = get_duration(visit)
        non_closed_visits.append({
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": format_duration(duration)
        })
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
