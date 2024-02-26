from django.urls import path

from sale.views import category_views, product_of_user_views, product_views, request_views, transaction_views, user_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user', user_views.UserIndex),
    path('user/create', user_views.UserStore),
    path('user/<int:pk>', user_views.UserShow),
    path('user/update/<int:pk>', user_views.UserUpdate),
    path('user/delete/<int:pk>', user_views.UserDelete),

    path('category', category_views.CategoryIndex),
    path('category/create', category_views.CategoryStore),
    path('category/<int:pk>', category_views.CategoryShow),
    path('category/update/<int:pk>', category_views.CategoryUpdate),
    path('category/delete/<int:pk>', category_views.CategoryDelete),

    path('product', product_views.ProductIndex),
    path('product/create', product_views.ProductStore),
    path('product/<int:pk>', product_views.ProductShow),
    path('product/update/<int:pk>', product_views.ProductUpdate),
    path('product/delete/<int:pk>', product_views.ProductDelete),

    path('productofuser', product_of_user_views.POUIndex),
    path('productofuser/create', product_of_user_views.POUStore),
    path('productofuser/<int:pk>', product_of_user_views.POUShow),
    path('productofuser/update/<int:pk>', product_of_user_views.POUUpdate),
    path('productofuser/delete/<int:pk>', product_of_user_views.POUDelete),

    path('transaction', transaction_views.TransactionIndex),
    path('transaction/create', transaction_views.TransactionStore),
    path('transaction/<int:pk>', transaction_views.TransactionShow),
    path('transaction/update/<int:pk>', transaction_views.TransactionUpdate),
    path('transaction/delete/<int:pk>', transaction_views.TransactionDelete),

    path('request', request_views.RequestIndex),
    path('request/create', request_views.RequestStore),
    path('request/<int:pk>', request_views.RequestShow),
    path('request/update/<int:pk>', request_views.RequestUpdate),
    path('request/delete/<int:pk>', request_views.RequestDelete),

]