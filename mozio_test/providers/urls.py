# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from rest_framework.routers import SimpleRouter


from . views import ProviderViewSet, ServiceAreaViewSet


app_name = 'providers'

router = SimpleRouter()

router.register('providers', ProviderViewSet)
router.register('service-area', ServiceAreaViewSet)

urlpatterns = router.urls
