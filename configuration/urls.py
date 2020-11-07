# from rest_framework import routers
from django.urls import path
from .api import SiteInformationAPI, PayPalKeysAPI, FacebookKeysAPI, GoogleKeysAPI

# router = routers.DefaultRouter()
# router.register('api/site_configuration', SiteConfigurationAPI, 'site_configuration')

urlpatterns = [
  path('api/get_site_info', SiteInformationAPI.as_view(), name='get_site_info'),
  
  path('api/auth/paypal_keys', PayPalKeysAPI.as_view(), name='paypal_keys'),
  path('api/auth/facebook_keys', FacebookKeysAPI.as_view(), name='facebook_keys'),
  path('api/google_keys', GoogleKeysAPI.as_view(), name='google_keys'),
]

# urlpatterns += router.urls