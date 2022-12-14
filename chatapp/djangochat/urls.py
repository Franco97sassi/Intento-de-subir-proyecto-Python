from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls'))
# path('farm/chat', nombre funcion en view,(chat interno))
]
