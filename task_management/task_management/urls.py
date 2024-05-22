from django.contrib import admin
from django.urls import path, include
from project_task.views import homeView, custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('', include('project_task.urls')), 
    path('api/', include('api.urls')),
]

handler404 = 'project_task.views.custom_404_view'
