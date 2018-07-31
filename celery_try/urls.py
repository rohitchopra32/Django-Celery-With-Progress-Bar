from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'celery_try.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('index/', include('testapp.urls')),
]
