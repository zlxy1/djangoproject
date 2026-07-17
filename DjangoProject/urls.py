from django.contrib import admin
from django.urls import path,include
from myProject1.views import staff_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myProject1.urls")),

]