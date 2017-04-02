from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
