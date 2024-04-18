from django.urls import path

from ad_infomation import views

urlpatterns = [
    path('create_ads/', views.create_ads, name='ads_detail'),
    path('get_ads/<int:pk>/', views.get_ads, name='get_ads'),
    path('get_all_ads/', views.get_all_ads, name='get_all_ads'),
    path('delete_a_ads/<int:pk>/', views.delete_ads, name='delete_a_ads'),
    path('update_a_ads/<int:pk>/', views.update_ads, name='update_a_ads'),
]
