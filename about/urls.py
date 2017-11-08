from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$',TemplateView.as_view(template_name='about/about.html'),name=index)
    url(r'^$', views.index, name='index'),
    url(r'^project$',views.project,name='project')
]
