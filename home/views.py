from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, CartItem
from django.shortcuts import redirect
from .models import Product, CartItem

def home(request):
    return render(request, 'index.html')

def phone(request):
    return render(request, 'phone.html')

def mac(request):
    return render(request, 'mac.html')

def pad(request):
    dict_pro={
        'pad_pro': Product.objects.all()

    }
    return render(request, 'pad.html',dict_pro)

def accessories(request):
    return render(request, 'accessories.html')

def loginn(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect('login')

    return render(request, 'signup.html')






def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    for p in product:
        image= p.image
        price=p.price


    # Check if the product is already in the user's cart
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        # If the item already exists in the cart, increment the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page or wherever you want


def products(request):
    dict_pro={
        'pad_pro': products.objects.all()

    }
    return render(request, 'pad.html',dict_pro)
     

