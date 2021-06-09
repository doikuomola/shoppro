from django.contrib import admin
from django.urls import path, include
from account.views import login_view, register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('products.urls', namespace='products')),
    path('', include('account.urls', namespace='accounts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
