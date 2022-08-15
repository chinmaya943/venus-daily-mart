from itertools import product
from pyclbr import Function
from unicodedata import category
from django import views
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views import View
from  .models import CASHIER, MANAGER, STAFF_CATEGORY_CHOICES, Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse
# For Function based login view
from django.contrib.auth.decorators import login_required
# For Class based login view
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from .models import Product, Cart, Customer, OrderPlaced, User
from django.template import RequestContext
from django.contrib.auth.hashers import make_password



# Admin Views

class CustomLoginView(auth_views.LoginView):
    template_name = 'app/login.html'
    success_url = '/dologin'

#login page
def login(request):
    if request.user.is_superuser:
        return redirect('admin-home')
    elif request.user.staff_category == MANAGER:
        return render(request, 'staff/staff_home.html')
    elif request.user.staff_category == CASHIER:
        return render(request, 'cash_counter/cashier_home.html')
    else:
        return redirect('home')

def dashboard(request):
    return render(request, 'admin_app/admin_home.html')

# Staff view
def staff_dashboard(request):
    return render(request, 'staff/staff_home.html')

# Cashier view
def cashier_dashboard(request):
    return render(request, 'cash_counter/cashier_home.html')


# Product View list(Admin)
def all_products(request):
    product_list = Product.objects.all()
    return render(request, 'admin_app/products.html', {'product_list':product_list})

# Product View list(Staff)
def all_product(request):
    products_list = Product.objects.all()
    return render(request, 'staff/products.html', {'products_list':products_list})

# Product View list(cashier)
def all_productss(request):
    productss_list = Product.objects.all()
    return render(request, 'cash_counter/products.html', {'productss_list':productss_list})

# Cart View list(Admin)
def all_carts(request):
    cart_list = Cart.objects.all()
    return render(request, 'admin_app/carts.html', {'cart_list':cart_list})

# Cart View list(Staff)
def all_cart(request):
    carts_list = Cart.objects.all()
    return render(request, 'staff/carts.html', {'carts_list':carts_list})

# Customer View list(Admin)
def all_customer(request):
    customer_list = Customer.objects.all()
    return render(request, 'admin_app/customers.html', {'customer_list':customer_list})

# Customer View list(Staff)
def all_customeres(request):
    customers_list = Customer.objects.all()
    return render(request, 'staff/customers.html', {'customers_list':customers_list})


# Order-Placed list(Admin)
def all_orderplaced(request):
    orderplaced_list = OrderPlaced.objects.all()
    return render(request, 'admin_app/order_placed.html', {'orderplaced_list':orderplaced_list})

# Order-Placed list(Staff)
def all_orderplace(request):
    orderplace_list = OrderPlaced.objects.all()
    return render(request, 'staff/order_placed.html', {'orderplace_list':orderplace_list})


# Users list(Admin)
def all_users(request):
    users_list = User.objects.all()
    # print(users_list)
    return render(request, 'admin_app/users.html', {'users_list':users_list})

# Users list(Staff)
def all_user(request):
    user_list = User.objects.all()
    # print(user_list)
    return render(request, 'staff/users.html', {'user_list':user_list})


# Bill-page
def bill_page(request):
    return render(request, 'admin_app/bills.html')

# Product insert(Admin)
def productinsert(request):
    if request.method == 'POST':
        if request.POST.get('group') and request.POST.get('item_type') and request.POST.get('supplier') and request.POST.get('manufacturer') and request.POST.get('title') and request.POST.get('barcode') and request.POST.get('item_size') and request.POST.get('item_color') and request.POST.get('purchase_price') and request.POST.get('purchase_tax') and request.POST.get('selling_price') and request.POST.get('selling_tax') and request.POST.get('discounted_price') and request.POST.get('description') and request.POST.get('brand') and request.POST.get('category') and request.POST.get('actual_mrp') and request.POST.get('product_purchase_date') and request.POST.get('expiry_date') and request.POST.get('product_image'):           
            
            toBeSaved = Product()
            toBeSaved.group = request.POST.get('group')
            toBeSaved.item_type = request.POST.get('item_type')
            toBeSaved.supplier = request.POST.get('supplier')
            toBeSaved.manufacturer = request.POST.get('manufacturer')
            toBeSaved.title = request.POST.get('title')
            toBeSaved.barcode = request.POST.get('barcode')
            toBeSaved.item_size = request.POST.get('item_size')
            toBeSaved.item_color = request.POST.get('item_color')
            toBeSaved.purchase_price = request.POST.get('purchase_price')
            toBeSaved.purchase_tax = request.POST.get('purchase_tax')
            toBeSaved.selling_price = request.POST.get('selling_price')
            toBeSaved.selling_tax = request.POST.get('selling_tax')
            toBeSaved.discounted_price = request.POST.get('discounted_price')
            toBeSaved.description = request.POST.get('description')
            toBeSaved.brand = request.POST.get('brand')
            toBeSaved.category = request.POST.get('category')
            toBeSaved.actual_mrp = request.POST.get('actual_mrp')
            toBeSaved.product_purchase_date = request.POST.get('product_purchase_date')
            toBeSaved.expiry_date = request.POST.get('expiry_date')
            toBeSaved.product_image = request.POST.get('product_image')
            toBeSaved.save()
            messages.success(request, 'Product Inserted Successfully......!!!')
            return HttpResponseRedirect(request, 'admin_app/productinsertform.html')
    else:
        return render(request, 'admin_app/productinsertform.html')

# Product insert(Staff)
def product_insert(request):
    if request.method == 'POST':
        if request.POST.get('group') and request.POST.get('item_type') and request.POST.get('supplier') and request.POST.get('manufacturer') and request.POST.get('title') and request.POST.get('barcode') and request.POST.get('item_size') and request.POST.get('item_color') and request.POST.get('purchase_price') and request.POST.get('purchase_tax') and request.POST.get('selling_price') and request.POST.get('selling_tax') and request.POST.get('discounted_price') and request.POST.get('description') and request.POST.get('brand') and request.POST.get('category') and request.POST.get('actual_mrp') and request.POST.get('product_purchase_date') and request.POST.get('expiry_date') and request.POST.get('product_image'):           

            toBeSaved = Product()
            toBeSaved.group = request.POST.get('group')
            toBeSaved.item_type = request.POST.get('item_type')
            toBeSaved.supplier = request.POST.get('supplier')
            toBeSaved.manufacturer = request.POST.get('manufacturer')
            toBeSaved.title = request.POST.get('title')
            toBeSaved.barcode = request.POST.get('barcode')
            toBeSaved.item_size = request.POST.get('item_size')
            toBeSaved.item_color = request.POST.get('item_color')
            toBeSaved.purchase_price = request.POST.get('purchase_price')
            toBeSaved.purchase_tax = request.POST.get('purchase_tax')
            toBeSaved.selling_price = request.POST.get('selling_price')
            toBeSaved.selling_tax = request.POST.get('selling_tax')
            toBeSaved.discounted_price = request.POST.get('discounted_price')
            toBeSaved.description = request.POST.get('description')
            toBeSaved.brand = request.POST.get('brand')
            toBeSaved.category = request.POST.get('category')
            toBeSaved.actual_mrp = request.POST.get('actual_mrp')
            toBeSaved.product_purchase_date = request.POST.get('product_purchase_date')
            toBeSaved.expiry_date = request.POST.get('expiry_date')
            toBeSaved.product_image = request.POST.get('product_image')
            toBeSaved.save()
            messages.success(request, 'Product Inserted Successfully......!!!')
            return HttpResponseRedirect(request, 'staff/productinsertform.html')
    else:
        return render(request, 'staff/productinsertform.html')


# Customer insert
def customerinsert(request):
    if not request.user.is_superuser:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if request.method  == 'POST':
        if request.POST.get('user') and request.POST.get('name') and request.POST.get('locality') and request.POST.get('city') and request.POST.get('zipcode') and request.POST.get('state'):
            toBeS = Customer()
            toBeS.user = request.POST.get('user')
            toBeS.name = request.POST.get('name')
            toBeS.locality = request.POST.get('locality')
            toBeS.city = request.POST.get('city')
            toBeS.zipcode = request.POST.get('zipcode')
            toBeS.state = request.POST.get('state')
            toBeS.save()
            messages.success(request, 'Customer Inserted Successfully..!!')
            return render(request, 'admin_app/customerinsertform.html')
    else:
        return render(request, 'admin_app/customerinsertform.html')

# Cart insert
def cartinsert(request):
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('product') and request.POST.get('quantity'):
            addtocart = Cart()
            addtocart.user = request.POST.get('user')
            addtocart.product = request.POST.get('product')
            addtocart.quantity = request.POST.get('quantity')
            addtocart.save()
            messages.success(request, 'Cart Inserted Successfully..!!')
            return render(request, 'admin_app/cartinsertform.html')
    else:
        return render(request, 'admin_app/cartinsertform.html')

# Orderplaced insert
def order_placed(request):
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('customer') and request.POST.get('product') and request.POST.get('quantity') and request.POST.get('order_data') and request.POST.get('status'):
            toBeSave = OrderPlaced()
            toBeSave.user = request.POST.get('user')
            toBeSave.customer = request.POST.get('customer')
            toBeSave.product = request.POST.get('product')
            toBeSave.quantity = request.POST.get('quantity')
            toBeSave.order_date = request.POST.get('order_date')
            toBeSave.status = request.POST.get('status')
            toBeSave.save()
            messages.success(request, 'Order Placed Data Inserted Successfully..!!')
            return render(request, 'admin_app/opinsert.html')
    else:
        return render(request, 'admin_app/opinsert.html')

# Users insert
def user_insert(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('username') and request.POST.get('password') and request.POST.get('confirm_password') and request.POST.get('staff_category'):
            toBeSav = User()
            toBeSav.first_name = request.POST.get('first_name')
            toBeSav.last_name = request.POST.get('last_name')
            toBeSav.email = request.POST.get('email')
            toBeSav.username = request.POST.get('username')
            toBeSav.password = make_password(request.POST.get('password'))
            # toBeSav.confirm_password = request.POST.get('confirm_password')
            toBeSav.staff_category = request.POST.get('staff_category')
            toBeSav.save()
            messages.success(request, 'User Inserted Successfully..!!')
            return render(request, 'admin_app/userinsertform.html')
        else:
            messages.error(request, 'All fields are required')
            return render(request, 'admin_app/userinsertform.html')
    else:
        return render(request, 'admin_app/userinsertform.html')

# Update product
def update_product(request):
    product = Product.objects.get()
    return render(request, 'admin_app/update_product.html', {'product':product})

# User Views
#Home/Product view
class ProductView(View):
    def get(self, request):
        KitchenSteelproduct = Product.objects.filter(category='Kitchen Steelproduct')
        Grocery = Product.objects.filter(category='Grocery')
        Vegitables = Product.objects.filter(category='Vegitables')
        FreshFruits = Product.objects.filter(category='Fresh Fruits')
        Snacks = Product.objects.filter(category='Snacks')
        ColdDrinks = Product.objects.filter(category='Cold Drinks')
        DryfruitsNuts = Product.objects.filter(category='Dryfruits & Nuts')
        HotDrinks = Product.objects.filter(category='Hot Drinks') 
        Protins = Product.objects.filter(category='Protins')
        BeautyProducts = Product.objects.filter(category='Beauty Products')
        OtherHomeProdects = Product.objects.filter(category='Other Home Products')
        return render(request, 'app/home.html', {'KitchenSteelproduct':KitchenSteelproduct, 'Grocery':Grocery, 'Vegitables':Vegitables, 'FreshFruits':FreshFruits, 'Snacks':Snacks, 'ColdDrinks':ColdDrinks, 'DryfruitsNuts':DryfruitsNuts, 'HotDrinks':HotDrinks, 'Protins':Protins, 'BeautyProducts':BeautyProducts, 'OtherHomeProdects':OtherHomeProdects})

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart}) 

# search Function
def searchbar(request):
    if request.method =='GET':
        search = request.GET.get('search')
        prod = Product.objects.all().filter(title=search)
        return render(request, 'app/searchbar.html', {'prod':prod})

#add to cart
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

#view cart
@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)

        #calculation/no product in cart
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')
# Plus cart quantity & amount
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount


        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

# Minus cart quantity & amount
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount

            }
        return JsonResponse(data)

#  Minus cart quantity & amount
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

#buy now function
def buy_now(request):
    return render(request, 'app/buynow.html')

#address view
@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

# Orders
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})

#procuct view
#mobile Cold Drinks
# def mobile(request, data=None):
#     mobiles = []
#     if data == None:
#         mobiles = Product.objects.filter(category='M')
#     elif data == 'Redmi' or data == 'Samsung' or data == 'Iphone' or data == 'Vivo' or data == 'Oppo':
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     elif data =='Below':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
#     elif data =='Above':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
#     return render(request, 'app/mobile.html', {'mobiles':mobiles})


def admin_home(request):
    return render(request, 'admin_app/admin_home.html')

def staff_home(request):
    return render(request, 'staff/staff_home.html')

def cashier_home(request):
    return render(request, 'cash_counter/cashier_home.html')

#registration page
class CustomerRegistrationFormView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations..! Registered Successfully')
        return render(request, 'app/customerregistration.html', {'form':form})    

#checkout page
@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

# user profile page
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations..!! ProfileUpdated Successfully.')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

