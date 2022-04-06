from django.contrib import admin
from django.urls import path, include
import homepage.urls
import catalog.urls
import about.urls
import users.urls
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('auth/', include('users.urls')),
]
