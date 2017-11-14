
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Helloworld/', include('Helloworld.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^MLComponent/',include('MLComponent.urls')),
]
