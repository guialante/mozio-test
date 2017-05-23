# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Provider(models.Model):
    """
        Provider Model, represents a any provider into the site        
    """

    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
    language = models.CharField(max_length=255, default='English', verbose_name='Language')
    currency = models.CharField(max_length=10, default='USD', verbose_name='Currency')

    def __str__(self):
        return str(self.name)


@python_2_unicode_compatible
class ServiceArea(models.Model):
    """
        Service Area Model, represents the service area of the provider, a provider can have one or several
         service area
    """
    name = models.CharField(max_length=255, verbose_name='Name')
    price = models.FloatField(default=0.0, verbose_name='Price')
    area = models.PolygonField(verbose_name='Area')
    provider = models.ForeignKey(Provider, related_name='services_areas')
    objects = models.GeoManager()

    def __str__(self):
        return str(self.name)


