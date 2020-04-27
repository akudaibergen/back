from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from core.views import *
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('products/', ProductsList.as_view()),
    path('products/<int:comp_id>/', product_detail),
    path('reviews/', reviews_list),
    path('sproducts/', ProductLAPIView.as_view()),
    path('orders/', OrdersListAPIView.as_view()),
    path('users/',UserViewSet.as_view())
]