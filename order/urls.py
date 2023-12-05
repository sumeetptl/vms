from .views import PurchaseOrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'purchaseorders', PurchaseOrderViewSet, basename='purchase-order')
urlpatterns = router.urls