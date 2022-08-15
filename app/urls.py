from re import template
from django.conf import settings
from django.urls import include, path, reverse
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.views.generic import RedirectView
from django.contrib import admin
from . import api



urlpatterns = [
    
    path('', views.ProductView.as_view(), name="home"),
    path('dologin/', views.login, name='dologin'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('product\\-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart), 
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),   
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('registration/', views.CustomerRegistrationFormView.as_view(), name='customerregistration'),

    # for admin
    path('admin-home/', views.admin_home, name="admin-home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('products', views.all_products, name="list-products"),
    path('carts', views.all_carts, name="list-carts"),
    path('customers', views.all_customer, name="list-customers"),
    path('order-placed', views.all_orderplaced, name="list-order_placed"),
    path('users', views.all_users, name="list-users"),
    path('bills', views.bill_page, name="list-bills"),
    path('add-product', views.productinsert, name="P-insert"),
    path('add-customer', views.customerinsert, name="Cu-insert"),
    path('add-cart', views.cartinsert, name="Ca-insert"),
    path('add-order_placed', views.order_placed, name="Op-insert"),
    path('add-users', views.user_insert, name="U-insert"), 

    # path('update_product', views.update_product, name='update-product'),

    # for staff
    path('staff-home/', views.staff_home, name= "staff-home"),
    path('staff_dashboard', views.staff_dashboard, name="staff_dashboard"),
    path('product', views.all_product, name="lists-products"),
    path('add-products', views.product_insert, name="Product-insert"),
    path('cartss', views.all_cart, name="lists-carts"),
    path('customer', views.all_customeres, name="list-customeress"),
    path('order-place', views.all_orderplace, name="list-order_place"),
    path('user', views.all_user, name="list-user"),
    path('bills', views.bill_page, name="list-bills"),

    # for cashier
    path('cashier-home/', views.cashier_home, name="cashier-home"),
    path('productss', views.all_productss, name="list-productss"),
    path('bills', views.bill_page, name="list-bills"),


    # path('api/', include(router.urls)),
    path('api/product', api.filter_product),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
