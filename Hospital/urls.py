"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("go-to-github/", RedirectView.as_view(url='https://github.com/Evgeniy994'), name='go-to-github'),
    path("go-to-linkedin/", RedirectView.as_view(url='https://www.linkedin.com/in/evgeny-tretiak-61659b243/'), name='go-to-linkedin'),
    path("go-to-cv/",
         RedirectView.as_view(url='https://drive.google.com/file/d/1qOYDBxY7Nj8NLnVVAEeM2UAH4RrsFYDl/view'),
         name='go-to-cv'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
