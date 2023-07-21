from django.contrib import admin
from .models import customers,gallery,Cart,OrderDetails
# Register your models here.
admin.site.register(customers)
admin.site.register(gallery)


class AdminCart(admin.ModelAdmin):
    list_display=['id','email','product','image','price']
class OrderDetailsCart(admin.ModelAdmin):
    list_display=['id','user','image','product_name','price','quantity','ordered_date','status']

admin.site.register(Cart,AdminCart)
admin.site.register(OrderDetails,OrderDetailsCart)