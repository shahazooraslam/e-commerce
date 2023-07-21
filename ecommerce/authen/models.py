from django.db import models



STATUS1=(
    ("ACCEPTED","ACCEPTED"),
    ("PACKED","PACKED"),
    ("ON THE WAY","ON THEWAY"),
    ("DELIVERED","DELIVERD"),
    ("CANCELED","CANCELED"),

)
# Create your models here.
class customers(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=14)
    confirmpassword=models.CharField(max_length=14)
    name=models.CharField(max_length=14)
    def __str__(self):
        return self.email
class gallery(models.Model):
    image=models.ImageField(upload_to="images/")
    description=models.TextField(max_length=255)
    sellingprice=models.IntegerField(default=0)
    discountprice=models.IntegerField(default=0)

    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    email=models.EmailField()
    product=models.ForeignKey(gallery,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)
    @property
    def pricee(self):
        new_price=self.product.discountprice * self.quantity
        return new_price
 

    


class OrderDetails(models.Model):
    user=models.EmailField()
    
    product_name=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=45,default="pending",choices=STATUS1)
     

    # @property
    # def get_cart_deal_total(self):
    #     orderitem = self.or.all()
    #     total = sum(item.get_deal_total for item in orderitem)
    #     return total