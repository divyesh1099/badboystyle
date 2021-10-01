"""badboystyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cart/', include('cart.urls')),
    # path('formal/', include('formal.urls')),
    # path('jean/', include('jean.urls')),
    path('product/', include('product.urls')),
    # path('shirt/', include('shirt.urls')),
    # path('short/', include('short.urls')),
    # path('tshirt/', include('tshirt.urls')),
]+static(settings.STATIC_URL, docoment_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Badboy Style Admin"
admin.site.site_title = "Badboy Style Admin Portal"
admin.site.index_title = "Welcome to Badboy Style Admin Portal"