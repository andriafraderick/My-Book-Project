from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_home'),

    path('register/', views.register_user, name='user_register'),
    path('login/', views.login_user, name='user_login'),
    path('logout/', views.logout_user, name='user_logout'),

    path('books/', views.book_list, name='user_book_list'),
    path('books/<int:book_id>/', views.book_details, name='user_book_details'),

    path('add_to_cart/<int:book_id>/', views.add_to_cart, name= "addtocart"),
    path('view_cart/', views.view_cart, name= 'viewcart'),
    path('increase/<int:item_id>/', views.increase_quantity, name= "increase_quantity"),
    path('decrease/<int:item_id>/', views.decrease_quantity, name= "decrease_quantity"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('create_cheackout_session/', views.create_checkout_session, name='create_cheackout_session'),
    path('success/',views.success, name='success'),
    path('cancel/', views.cancel, name='cancel')
]
