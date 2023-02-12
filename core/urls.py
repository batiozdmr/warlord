from django.contrib import admin

admin.site.site_header = 'CHAT BOT Yönetimi'
admin.site.index_title = 'CHAT BOT Yönetimi'
admin.site.site_title = 'CHAT BOT Yönetim Paneli'

from django.urls import include
from django.contrib import admin
from django.urls import path

from apps.mainpage.views import *

urlpatterns = (
    path('super/user/admin/', admin.site.urls),
    path('', include(('apps.mainpage.urls'), namespace='mainpage')),
    path('accounts/', include("allauth.urls")),

    path('parameter/', include("apps.parameter.urls")),

    path('ckeditor-secret/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),

)
