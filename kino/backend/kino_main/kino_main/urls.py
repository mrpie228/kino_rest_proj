
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from .yasg import urlpatterns as documentation_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v2/',include('movies.urls')),

    path('profiles/',include('user_profile.urls')),

    path('auth/',include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]

urlpatterns+=documentation_urls
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
