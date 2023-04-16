from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.CustomerListView.as_view(), name='list_clients'),
    #path('login/', views.login_user, name='login'),
    path('clients/add_client/', views.CustomerCreate.as_view(), name='add_client'),
    path('clients/<int:pk>/', views.CustomerDetails.as_view(), name='detail_client'),
    path('clients/update<int:pk>/', views.CustomerUpdate.as_view(), name='update_client'),
    path('clients/delete<int:pk>/', views.CustomerDelete.as_view(), name='delete_client')
    
]
