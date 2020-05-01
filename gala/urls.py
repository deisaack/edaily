from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from gala.pharmacy.views import ussd_callback, UserAuthViewset, PharmacyViewset, StaffViewset

router = DefaultRouter()
router.register("staff", StaffViewset, basename="staff")
router.register("pharmacy", PharmacyViewset, basename="pharmacy")
router.register("auth", UserAuthViewset, basename="auth")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ussd-callback/", ussd_callback),
]
urlpatterns += router.urls
urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)