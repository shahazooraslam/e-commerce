from django.shortcuts import render,redirect
# from . forms import SIGNUPFORM,LOGINFORM
from .models import customers,gallery,Cart,OrderDetails
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import razorpay
from django.views.decorators.csrf import csrf_exempt
# 
from django.contrib.auth import logout as logouts
from .models import gallery
from django.db.models import Q
from django.http import JsonResponse
# from django.contrib.auth import authenticate

# Create your views here.
def index(request):
     print("you are",request.session.get('email'))
     if request.session.has_key('email'):
          email=request.session["email"]
         
          
     else:
          return redirect('/login')
     totallength=0,
     name=0
     if request.session.has_key('email'):
          email=request.session["email"]
          totallength=len(Cart.objects.filter(email=email))
          name=customers.objects.filter(email=email)
          for n in name:
               namee=n.name
          data={
          
                    "totallength":totallength,
                    "name":namee
               }
     return render(request,"index.html",data)
def about(request):
     return render(request,"about.html")
def tshirts(request):
     image=gallery.objects.all()
     return render(request,"tshirts.html",{"image":image})

def signup(request):
    if request.method=="POST":
        
     #    if form.is_valid():
     #        name1=form.cleaned_data['name']
     #        email1=form.cleaned_data['email']
     #        password2=form.cleaned_data['password1']
     #        confirmpassword2=form.cleaned_data['confirmpassword1']
          name=request.POST["name"]
          email=request.POST["email"]
          password=request.POST["password"]
          confirmpassword=request.POST["confirmpassword"]
          try:
              user=customers.objects.filter(email=email).first()
              if user:
                    
                    messages.warning(request,"EMAIL ALREADY EXITS")
                    return redirect("/signup")
              elif (password!=confirmpassword):
                    messages.warning(request,"password doesnt match")
                    return redirect("/signup")
              else:
                    messages.success(request,"signup success")
                    add=customers(email=email,name=name,password=password,confirmpassword=confirmpassword)
                    add.save()
                    

                    subject = 'welcome to xyz'
                    message = f'Hi { name }, welcome to krabit.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect("/login")
          except:
               messages.warning(request,"email or password error")
               return redirect("/signup")
            

     


    return render(request,"signup.html")
def login(request):
    if request.method=="POST":
         
         
         
              email=request.POST["email"]
              password=request.POST["password"]
              try:
                   user=customers.objects.get(email=email)
                   if not  user:
                        messages.warning(request,"email doesnt exists")
                        return redirect("/login")
                   elif (user.password!=password):
                        messages.warning(request,"password error")
                        return redirect("/login")
                   else:
                        request.session["email"]=email
                        messages.success(request,"success")
                        subject = 'welcome to xyz'
                        message = f'Hi { email }, welcome to krabit.'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [email, ]
                        send_mail( subject, message, email_from, recipient_list )
                    # return redirect("/login")
                        return redirect("index")
              except:
                   messages.warning(request,"email or password error")
                   return redirect("/login")
    
         
    return render(request,"login.html")


def logout(request):
#     logouts(request)
#     messages.success(request,'SUCCESS')
#     return redirect('/')
      if request.session.has_key('email'):
           del request.session['email']
           return redirect("/")
# def cart(request):
#      return render(request,"cart.html")
def details(request,id):
     totallength=0
     image=gallery.objects.get(id=id)
     item_already_in_cart=False
     if request.session.has_key('email'):
          email=request.session["email"]
          item_already_in_cart=Cart.objects.filter(Q(product=image.id)&Q(email=email)).exists()
          totallength=len(Cart.objects.filter(email=email))
          data={
               "image":image,
                "item_already_in_cart":item_already_in_cart,
               "totallength":totallength
          }
     return render(request,"details.html",data)




def add_to_cart(request):
     email=request.session["email"]
     product_id=request.GET.get('prod_id')
     product_name=gallery.objects.get(id=product_id)
     product=gallery.objects.filter(id=product_id)

     for p in product:
          image=p.image
          price=p.discountprice
          Cart(email=email,product=product_name,image=image,price=price).save()
          return redirect(f"details/{product_id}")
def show_cart(request):
     totallength=0
     totalamount=0
     if request.session.has_key('email'):
          email=request.session["email"]
          totallength=len(Cart.objects.filter(email=email))
          customer=customers.objects.filter(email=email)
          for c in customer:
               name=c.name
               cart=Cart.objects.filter(email=email)
               
               
               
               data={
                         "name":name,
                         "totallength":totallength,
                         "cart":cart,
                         
                    
               }
               if cart:
                 return render(request,"show_cart.html",data)
               else:
                    return render(request,"empty_cart.html")
                    
                    

def plus_cart(request):
     if request.session.has_key("email"):
          email=request.session["email"]
          product_id=request.GET['prod_id']
          cart=Cart.objects.get(Q(product=product_id) &Q(email=email))
          
          cart.quantity+=1
          # totalamount=cart.quantity*cart.price
          
          cart.save()
          
          data={
               'quantity':cart.quantity,
          
               
          }
          return JsonResponse(data)
     
def minus_cart(request):
     if request.session.has_key("email"):
          email=request.session["email"]
          product_id=request.GET['prod_id']
          cart=Cart.objects.get(Q(product=product_id) &Q(email=email))
          cart.quantity-=1
          cart.save()
          
          data={
               'quantity':cart.quantity
               
          }
          return JsonResponse(data)
     

def remove_cart(request):
     if request.session.has_key("email"):
          email=request.session["email"]
          product_id=request.GET['prod_id']
          cart=Cart.objects.get(Q(product=product_id) &Q(email=email))
          
          cart.delete()
          
          
          
          return JsonResponse()
     return render(request,"index.html")

def checkout(request):
    if request.session.has_key("email"):
          totalamount=0
          email=request.session["email"]
          name=request.POST["name"]
          phone=request.POST["mobile"]
          address=request.POST["address"]
          print(email,name,phone,address)
          cart_product=Cart.objects.filter(email=email)
          for c in cart_product:
               product_name=c.product
               image=c.image
               quantity=c.quantity
               price=c.pricee
               totalamount+=c.pricee
               totalamount=totalamount*100
               OrderDetails(user=email,product_name=product_name,image=image,quantity=quantity,price=price).save()
               cart_product.delete()
               data={
                    "image":image,
                    "quantity":quantity,
                    "totalamount":totalamount

                }
               
          return render(request,"order.html",data)
#
#    
def order(request):
     if request.session.has_key("email"):
          totalamount=0
          email=request.session["email"]
          cart_product=Cart.objects.filter(email=email)
          for c in cart_product:
               totalamount+=c.pricee
     if request.method=="POST":
          amount=totalamount
          order_currency="INR"
          client=razorpay.Client(auth=("rzp_test_d6uwjQOhVC1IZZ","IZNHFDqe4OQtX6ejQ6AGxAxi"))
          payment=client.order.create({"amount":amount,"currency":"INR","payment_capture":1})
     return render(request,"order.html")

@csrf_exempt
def success(request):
     return render(request,"success.html")
def orderdetail(request):
     if request.session.has_key("email"):
          
          email=request.session["email"]
          order=OrderDetails.objects.filter(user=email)
          
       

               
          return render(request,"orderdetails.html",{"order":order})

                    
