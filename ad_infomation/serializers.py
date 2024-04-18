from rest_framework import serializers

from ad_infomation.models import Ads


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['title','description','price']
