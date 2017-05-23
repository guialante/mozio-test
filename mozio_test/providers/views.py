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
        retrieve:
        Return the given provider
        
        list:
        Return a list of all providers
        
        create:
        Create a new provider
        
        update:
        Update the given provider
        
        partial_update:
        Make a partial update of the given provider
        
        destroy:
        Delete the given provider        
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """    
        retrieve:
        Return the given service area

        list:
        Return a list of all service areas

        create:
        Create a new service area

        update:
        Update the given service area

        partial_update:
        Make a partial update of the given service area

        destroy:
        Delete the given service area
        
    """

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    @list_route(methods=['get'], url_path='search')
    def search(self, request):
        """        
        Return a queryset with the results of the search using lat and lng if the point exists, return empty
        queryset otherwise.
        
        Use as following example: /service-area/search/?lat=37.78441844686463&lng=-122.47266769409178
        
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
