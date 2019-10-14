"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from use_rest import urls # include를 통해 app의 urls에서 관리할 수 있게 해줌
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls # 이거 api-auth로 관리자페이지에서 간단하게 로그인아웃 할 수 있음

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('use_rest.urls')),
    path('api-auth/', include('rest_framework.urls')) # rest_framework의 page에서 쉽게 로그인아웃할 수 있도록 해줌
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
