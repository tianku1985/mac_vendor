from django.conf.urls import *
from main.views import *

urlpatterns = [
    url(r'^echo',echo),
	url(r'^get_mac_vendor',get_mac_vendor),
	url(r'^init_mac_database',init_mac_database),
	
]
