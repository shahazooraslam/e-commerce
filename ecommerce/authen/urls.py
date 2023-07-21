from django.contrib import admin
from django.urls import path,include
from authen import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("signup/",views.signup,name="/signup"),
    path("login/",views.login,name="/login"),
    path("logout/",views.logout,name="logout/"),
    path("show_cart/",views.show_cart,name="/show_cart"),
    path("logout",views.logout,name="logout"),
    path("",views.index,name="index"),
    path("about",views.about,name="/about"),
    path("tshirts",views.tshirts,name="/tshirts"),
    path("details/<int:id>",views.details,name="details"),
    path("add_to_cart",views.add_to_cart,name="add_to_cart"),
    path("plus_cart",views.plus_cart,name="plus_cart"),
    path("minus_cart",views.minus_cart,name="minus_cart"),
    path("remove_cart",views.remove_cart,name="remove_cart"),
    path("checkout",views.checkout,name="checkout"),
    path("order",views.order,name="order"),
    path("success",views.success,name="success"),
    path("orderdetail",views.orderdetail,name="orderdetail"),
    # path("emptyorder",views.emptyorder,name="orderdetail"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)