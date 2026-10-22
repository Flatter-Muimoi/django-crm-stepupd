from django.urls import path
# インポートするビューが増える
from .views import (
    CustomerListView, 
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    ajax_add_activity,
)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    
    # 新規登録ページ
    path('customer/new/', CustomerCreateView.as_view(), name='customer_create'),
    
    # 更新ページ
    path('customer/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    
    # 削除ページ
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
     
     # Ajax処理⽤URL
        path('ajax/add_activity/', ajax_add_activity, name='ajax_add_activity'),
]
