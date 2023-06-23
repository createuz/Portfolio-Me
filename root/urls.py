from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from root.settings import STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
