from rest_framework import serializers

from .models import SellerDetails_Model,GetLinks_Model


class SellerDetails_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SellerDetails_Model
        fields = "__all__"


class GetLinks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GetLinks_Model
        fields = "__all__"
