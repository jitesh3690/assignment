from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_task.urls')), 
    path('api/', include('api.urls')),
]