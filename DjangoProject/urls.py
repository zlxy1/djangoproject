from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myProject1.urls")),

    path('account/', include('account.urls')),

]