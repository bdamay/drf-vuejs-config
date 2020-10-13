from django.urls import include, path, re_path
from django.contrib import admin

from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('vue', views.vue, name='vue'),

]

#API URLS
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
   # path('api/auth/', include('rest_framework.urls', namespace='rest_framework_api'))
]