from django.urls import path
from . import views

urlpatterns = [
    path('nouCarreto/', views.nouCarreto, name='nouCarreto'),
    path('afegirProducte/', views.afegirProducte, name='afegirProducte'),
    path('eliminarProducte/<int:pk>', views.eliminarProducte, name='eliminarProducte'),
    path('eliminarCarreto/<int:pk>', views.eliminarCarreto, name='eliminarCarreto'),
    path('modificarQuantitatProducte/<int:pk>', views.modificarQuantitatProducte, name='modificarQuantitatProducte'),
    path('llistatProductesCarreto/<int:pk>', views.llistatProductesCarreto, name='llistatProductesCarreto'),
    path('comprar/<int:pk>', views.comprar, name='comprar'),
]