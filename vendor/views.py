from rest_framework import viewsets
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer

# Create your views here.
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
