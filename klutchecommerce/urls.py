from .views import CustomersViewSet, ProductsViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers/', CustomersViewSet)
router.register(r'products/', ProductsViewSet)
router.register(r'orders/', OrderViewSet)
urlpatterns = router.urls

