
from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('facinfo/<int:pk>', views.facebook_detail),
    path('facinfo/', views.facebook_list),

]
