from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepageview, name='home'),
    path('shoppinglist/', views.shoppinglistview, name='shoppinglist'),
    path('add-shoppinglist-item/', views.addshoppinglistitem,
         name='addshoppinglistitem'),
    path('done-shoppinglist-item/<int:shoppinglist_item_id>/',
         views.doneshoppinglistitem, name='doneshoppinglistitem'),
    path('undone-shoppinglist-item/<int:shoppinglist_item_id>/',
         views.undoneshoppinglistitem, name='undoneshoppinglistitem'),
    path('delete-shoppinglist-item/<int:shoppinglist_item_id>/',
         views.deleteshoppinglistitem, name='deleteshoppinglistitem'),
]
