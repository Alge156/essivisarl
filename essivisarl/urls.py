
from django.contrib import admin
from django.urls import path,include
from authentification import views
from . import views


# from Commercialapi import views




from rest_framework import routers

from Commercialapi.views import CommercialAPIViewset
from Commercialapi.views import ClientAPIviewset
from Commercialapi.views import DepotAPIviewset
from Commercialapi.views import ProduitAPIviewset
from Commercialapi.views import CommandeAPIviewset
# creation du routeur
router= routers.SimpleRouter()


router.register('commercial', CommercialAPIViewset, basename='commercial')

router.register('client', ClientAPIviewset, basename='client')

router.register('depot', DepotAPIviewset, basename='depot')

router.register('produit', ProduitAPIviewset, basename='produit')


router.register('commande', CommandeAPIviewset, basename='commande')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('connexion/',  views.admin_view),
    path('authentification/', include('django.contrib.auth.urls')),
    path('authentification/', include('authentification.urls')),
    path('commercial/', include(router.urls)),
    path('client/', include(router.urls)),
    path('depot/', include(router.urls)),
    path('produit/', include(router.urls)),
    path('commande/', include(router.urls))
    
    # path('commercial/', views.commercial_list),
    # path('commercial/<int:id>/', views.commercial_detail)
    


]
