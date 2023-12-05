from rest_framework import serializers
from vendor.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields= '__all__'
        
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Vendor.objects.create(**validated_data)
