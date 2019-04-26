from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from studiomanna.views import PageWithEventsView

admin.site.site_header = 'Studio Manna'
admin.site.site_title = 'Studio Manna'

urlpatterns = []

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', PageWithEventsView.as_view(), {'slug': ''}, name='homepage'),
    path('<slug:slug>/', PageWithEventsView.as_view(), name='page'),
    path('', include('cms.urls', namespace='cms')),
]
