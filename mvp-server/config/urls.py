from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # my app
    path('api/', include('api.urls'), name='api'),
]
