from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('myabout/', about, name="about"),
    path('student/information/', student_information, name='student_information'),
    path('product/page/', product_create, name='product_create'),
    path('product/page/create/', product_create2, name='product-create'),
    path('user/signup/', signup, name ="signup"),
    # path('user/login', login_view , name="login" ),
    path('user/logout/', logout_views , name="log_out" ),
    path('user/change/password/', passwordchange, name = 'passwordchange'),
    path('product/details/<int:id>/', product_details, name = 'product_details'),
    path('product/details/<slug>/', product_details, name = 'product-details'),
    path('product/update/<int:pk>/', product_update, name = 'product_update'),
    path('product/delete/<int:pk>/', product_delete, name = 'product_delete'),
    path('user/login/class/', LoginViewClassBase.as_view(), name="login_class"),

    path('category/page/', category, name = "category")
]
