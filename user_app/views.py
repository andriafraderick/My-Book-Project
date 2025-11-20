from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from book_app.models import Book  

from django.core.paginator import Paginator, EmptyPage

from .models import Cart,CartItem

import stripe
from django.conf import settings
from django.urls import reverse


# ---------------- REGISTER ----------------
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('user_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('user_register')

        User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "Registration successful! Please login.")
        return redirect('user_login')

    return render(request, 'user/register.html')

# ---------------- LOGIN ----------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('user_book_list')
        else:
            messages.error(request, "Invalid login details")
            return redirect('user_login')

    return render(request, 'user/login.html')

# ---------------- LOGOUT ----------------
def logout_user(request):
    auth.logout(request)
    return redirect('user_login')

# ---------------- USER HOME ----------------
def user_dashboard(request):
    return redirect('user_login')

# ---------------- BOOK LIST ----------------
def book_list(request):

    books = Book.objects.all().order_by('id')

    paginator = Paginator(books,4)
    page_number = request.GET.get('page')

    try:
         page= paginator.get_page(page_number)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    return render(request, 'user/book_list.html', { 'page': page})



# ---------------- BOOK DETAILS ----------------
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'user/book_details.html', {'book': book})


def home(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})




def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.quantity > 0:
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            book=book
        )

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('viewcart')

    else:
        return HttpResponse("Out of stock")
  
    


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.book.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_items': total_items
    }

    return render(request, 'user/cart.html', context)
    


def increase_quantity(request, item_id):
    item = CartItem.objects.get(id=item_id)

    if item.quantity < item.book.quantity:
        item.quantity += 1
        item.save()

    return redirect("viewcart")  



def decrease_quantity(request, item_id):
    item = CartItem.objects.get(id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("viewcart")   



def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect("viewcart")  



def create_checkout_session(request):

    cart_items = CartItem.objects.all()

    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY  

        if request.method == 'POST':
            line_items = []

            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data': {
                            'currency': 'inr',
                            'unit_amount': int(cart_item.book.price * 100),  # price in paise
                            'product_data': {
                                'name': cart_item.book.title,   
                            },
                        },
                        'quantity': 1
                    }
                    line_items.append(line_item)

            if line_items:
                checkout_session = stripe.checkout.Session.create( 
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=request.build_absolute_url(reverse('success')),
                    cancel_url=request.build_absolute_url(reverse('cancel'))
                )

                return redirect(checkout_session.url, code=303)

    return redirect('viewcart')




def success(request):

    cart_items = CartItem.objects.all()

    for cart_item in cart_items:
        product = cart_item.book

        if product.quantity >= cart_item.quantity:

            product.quantity -= cart_item.quantity
            product.save()

    cart_items.delete()

    return render(request,'user/success.html')


def cancel(request):

    return render(request, 'user/cancel.html')