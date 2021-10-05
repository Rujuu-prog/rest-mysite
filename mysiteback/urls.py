from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_otp.admin import OTPAdminSite

urlpatterns = [
    path('edit/', admin.site.urls),
    path('api/', include('api.urls')),
    path('markdownx/', include('markdownx.urls')),
]
#保存されたファイルをurlのパスからアクセスできるようにする
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite