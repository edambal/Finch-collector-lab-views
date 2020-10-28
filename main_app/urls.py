from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('collectors/',views.collectors_index,name='collectors_index'),
    path('collectors/<int:collector_id>/',views.collectors_detail,name='detail'),
    path('collectors/<int:collector_id>/add_coin/',views.add_coin,name='addcoin')
]