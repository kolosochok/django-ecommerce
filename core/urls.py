from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [

	# Homepage
	path('', views.index, name='index'),
	
	# Product
	path('products/', views.products_list_view, name='products-list'),
	path('product/<pid>/', views.product_detail_view, name='products-detail'),

	# Category
	path('category/', views.category_list_view, name='category-list'),
	path('category/<cid>/', views.category_product_list_view, name='category-product-list'),

	# Vendor
	path('vendors/', views.vendor_list_view, name='vendor-list'),
	path('vendor/<vid>/', views.vendor_detail_view, name='vendor-detail'),

	# Tags
	path('products/tag/<slug:tag_slug>/', views.tags_list, name='tags'),

	# Add Product Review
	path('ajax-add-review/<int:pid>/', views.ajax_add_review, name='ajax-add-review'),

	# Seacrh 
	path('search/', views.search_view, name='search'),

	# Product Filter
	path('filter-product/', views.filter_product, name='filter-product'),

	# Add To Cart 
	path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

	# Cart Page
	path('cart/', views.cart_view, name='cart'),

	# Delete from cart
	path('delete-from-cart/', views.delete_from_cart, name='delete-from-cart'),

	# Update cart
	path('update-cart/', views.update_cart, name='update-cart'),

	# Wishlist page
	path('wishlist/', views.wishlist_view, name='wishlist'),

	# Add To Wishlist
	path('add-to-wishlist/', views.add_to_wishlist, name='add-to-wishlist'),

	# Remove From Wishlist
	path('remove-from-wishlist/', views.remove_from_wishlist, name='remove-from-wishlist'),

	# Contact
	path('contact/', views.contact, name='contact'),

	# Ajax Contact From
	path('ajax-contact-form/', views.ajax_contact_form, name='ajax-contact-form'),

	# About Us
	path('about/', views.about, name='about'),
]