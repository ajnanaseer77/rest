"""rest_new URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_new_app.views import Taskviewset,Createapiview
from rest_framework import routers
from rest_new_app import views

# router=routers.DefaultRouter()
router=routers.SimpleRouter()
router.register('task',Taskviewset)
router.register('completed_task',views.Completedtaskviewset)
router.register('due_task',views.Duetaskviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Createapiview.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',include(router.urls))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
