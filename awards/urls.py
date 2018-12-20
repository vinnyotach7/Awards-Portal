from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^loader/$', views.loader, name='loader'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profiles/(\d+)', views.profiles, name='profiles'),
    url(r'^projects/(\d+)', views.projects, name='projects'),

    url(r'^edit/profile/$', views.edit_profile, name='edit_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles', views.ProfileList.as_view()),
    url(r'^api/profile/(?P<pk>\d+)', views.ProfileDesc.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
