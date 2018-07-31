from django.urls import include, path
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'celery_try.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', views.index,name='index'),
    path('poll_state', views.poll_state,name='poll_state'),
]
