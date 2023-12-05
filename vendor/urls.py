from .views import VendorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
urlpatterns = router.urls