from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from gala.pharmacy.views import ussd_callback, UserAuthViewset, PharmacyViewset, StaffViewset

router = DefaultRouter()
router.register("staff", StaffViewset, )
router.register("pharmacy", PharmacyViewset, )
router.register("auth", PharmacyViewset, )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ussd-callback/", ussd_callback),
]
urlpatterns += router.urls
