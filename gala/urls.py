from django.contrib import admin
from django.urls import path
from gala.pharmacy.views import ussd_callback
urlpatterns = [
    path('admin/', admin.site.urls),
    path("ussd-callback/", ussd_callback),
]
