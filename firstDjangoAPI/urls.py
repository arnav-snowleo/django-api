from django.contrib import admin
from django.urls import path , include

from employeeapi.views import current_datetime_view

from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , current_datetime_view),
    path('api/', include(router.urls)),  # 'api/' is the base path
]
