from django.urls import path

from management.views import item_list, item_detail, item_new, item_edit, item_delete, client_list, client_detail, \
    client_new, client_edit, client_delete, button_down, button_up

app_name = 'management'


urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('item/new/', item_new, name='item_new'),
    path('item/edit/<int:pk>/', item_edit, name='item_edit'),
    path('item/delete/<int:pk>/', item_delete, name='item_delete'),

    path('client/', client_list, name='client_list'),
    path('client/<int:pk>/', client_detail, name='client_detail'),
    path('client/new/', client_new, name='client_new'),
    path('client/edit/<int:pk>/', client_edit, name='client_edit'),
    path('client/delete/<int:pk>/', client_delete, name='client_delete'),

    path('item/button_down/<int:pk>', button_down, name='button_down'),
    path('item/button_up/<int:pk>', button_up, name='button_up'),
]
