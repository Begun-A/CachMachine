from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cashmachine.views.home', name='home'),

    url(r'^', include('actions.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
