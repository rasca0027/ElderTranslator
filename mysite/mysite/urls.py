from django.conf.urls import include, url
from django.contrib import admin
from elder.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', index, name='index'),
    url(r'^test/', file_test),
    url(r'^callback/', bot_callback),
    url(r'^bot_test/', bot_test_view),
]
