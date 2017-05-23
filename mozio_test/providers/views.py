# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from django.contrib.gis.geos import Point


from . models import Provider, ServiceArea
from . serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
        Provider API View, this view has all the CRUD methods(endpoints) of the Provider
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
        Service Area API View, this view has all the CRUD methods(endpoints) of the Service Area
    """

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    @list_route(methods=['get'], url_path='search')
    def search(self, request):
        """
        
        :param request: 
        :return: queryset with the results of the search using lat and lng if the point exists, return empty
        queryset otherwise.
        """

        queryset = self.get_queryset()
        query_params = request.query_params
        lat = query_params.get('lat')
        lng = query_params.get('lng')
        if lat is not None and lng is not None:
            pnt = Point(float(lng), float(lat))
            queryset = queryset.filter(area__bbcontains=pnt)
        else:
            queryset = queryset.none()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
