import datetime
from cms.views import PageView
from .models import Event

class PageWithEventsView(PageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.datetime.today()
        events = Event.objects.filter(date__gte=today)
        context.update({
            'events': events,
        })
        return context
