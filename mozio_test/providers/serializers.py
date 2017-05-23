# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from . models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    """
        Serialize of the Provider model, use to render providers on the DB and to store providers using the API.
    """

    class Meta:
        model = Provider
        fields = ['name', 'email', 'phone_number', 'language', 'currency']


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """
        Serialize of the Service Area model, use to render service area on the DB and to service area providers using 
        the API.
    """

    service_area_provider = serializers.PrimaryKeyRelatedField(
        source='provider', queryset=Provider.objects.all(), write_only=True
    )
    provider = serializers.CharField(source='provider.name', read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = 'area'
        fields = ['name', 'price', 'area', 'service_area_provider', 'provider']
