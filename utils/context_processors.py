from django.utils import timezone


def today(request):
    now = timezone.now().date()
    return {'today': now}