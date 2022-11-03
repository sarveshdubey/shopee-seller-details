from rest_framework import serializers

from .models import SellerDetails_Model


class SellerDetails_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SellerDetails_Model
        fields = "__all__"

