from django.urls import path
from .views import HomeListView, NosotrosView, carta_pdf_view, \
    PrivacyPolicyView, TermsConditionsView, robots_txt


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    #path('carta/', CartaView.as_view(), name="carta"),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('carta/', carta_pdf_view, name='carta_pdf'),
    path('privacidad/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terminos/', TermsConditionsView.as_view(), name='terms_conditions'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
