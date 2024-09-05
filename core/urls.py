from django.urls import path
from .views import HomeListView, CartaView, NosotrosView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('carta/', CartaView.as_view(), name="carta"),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
]
