from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('collectors/',views.collectors_index,name='collectors_index'),
    path('collectors/add/',views.add_collector,name='addcollector'),
    path('collectors/<int:collector_id>/',views.collectors_detail,name='detail'),
    path('collectors/<int:collector_id>/add_coin/',views.add_coin,name='addcoin'),
    path('collectors/<int:collector_id>/assoc_symp/<int:symp_id>/', views.assoc_symp, name='assoc_symp'),
    path('collectors/<int:collector_id>/remove_symp/<int:symp_id>/', views.remove_symp, name='remove_symp'),

]