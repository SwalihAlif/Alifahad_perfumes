from django.shortcuts import render,redirect,get_object_or_404
from . models import Product, Variant
from category_app.models import Category
from django.contrib.auth.models import User
from . forms import ProductForm
from django.db.models import  F
from django.contrib import messages
import re
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Variant

from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models import CharField
# Create your views here.



def product_list(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('admin_login')  
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_management')  # Adjust as necessary
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = ProductForm()
        errors = None

    products_list = Product.objects.all()

    query = request.GET.get('q', '').strip()
    
   

    if query:
        products_list = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(category__category_name__icontains=query) 
        )

    # products_list = Product.objects.all().order_by('available_stock')
    paginator = Paginator(products_list, 8)  # Show 10 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    categories = Category.objects.all()
    
    return render(request, 'admin/product.html', {
        'form': form,
        'product': products,
        'categories': categories,
        'errors': errors,
        'query': query
    })


#=======================================================================================================================================

def edit_product(request, product_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('admin_login') 
    product = get_object_or_404(Product, id=product_id)
    errors = []
    if request.method == 'POST':
 
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category_instance = get_object_or_404(Category, id=category_id)
        # available_stock = request.POST.get('available_stock')
        # price = request.POST.get('price')
        offer = request.POST.get('offer')
        

        image_1 = request.FILES.get('image_1')
        image_2 = request.FILES.get('image_2')
        image_3 = request.FILES.get('image_3')

        

        if len(description) < 100:
            errors.append('Description must be less than 100 characters.')

        # if float(price) < 0:
        #     errors.append('Price cannot be negative.')

        # if re.search(r'\s', product_name):
        #     errors.append('Product name must not contain spaces.')

        for image in [image_1, image_2, image_3]:
            if image:
                if not image.name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                    errors.append(f'Image {image.name} is not a valid format. Only jpg, jpeg, and png are allowed.')

        if errors:
            return render(request, 'admin/edit_product.html', {
                'product': product,
                'categories': Category.objects.all(),
                'errors': errors,
            })
        
        product.product_name = product_name
        product.description = description
        product.category = category_instance
        # product.available_stock = available_stock
        # product.price = price
        product.offer_percentage = offer

        # Update images if files are provided
        if image_1:
            product.image_1 = image_1
        if image_2:
            product.image_2 = image_2
        if image_3:
            product.image_3 = image_3
        
        # Save the changes to the database
        product.save()

        # Redirect to the product management page or any other page
        return redirect('product_management')

    else:
        # Render the form with i
        return render(request, 'admin/edit_product.html', {
            'product': product,
            'categories': Category.objects.all(),  
            
        })
    
#=======================================================================================================================================
  
def toggle_product_listing(request, product_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('admin_login') 
    
    product = get_object_or_404(Product, id=product_id)
    product.is_listed = not product.is_listed
    product.save()
    return redirect('product_management')

#=======================================================================================================================================





def get_size_choices(category_name):
    if category_name == 'attar':
        return Variant.ATTAR
    elif category_name in ['perfume', 'body spray']:
        return Variant.PERFUME
    elif category_name == 'incense sticks':
        return Variant.STICKS
    return []

def variant_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    variants = Variant.objects.filter(product=product)
    size_choices = get_size_choices(product.category.category_name.lower())
    return render(request, 'admin/variant_list.html', {'product': product, 'variants': variants, 'size_choices': size_choices})

def add_variant(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size_choices = get_size_choices(product.category.category_name.lower())
    
    if request.method == "POST":
        size = request.POST.get("size", "").strip()
        price = float(request.POST.get("price", "").strip())
        stock = request.POST.get("stock", "").strip()

        if not size or not price or not stock:
            messages.error(request, "All fields are required.")
            return redirect('variant_list', product_id=product_id)
        

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messages.error(request, "Price and stock must be valid numbers.")
            return redirect('variant_list', product_id=product_id)

        if Variant.objects.filter(product=product, size=size).exists():
            messages.error(request, f"Size {size} already exists for this product.")
            return redirect('variant_list', product_id=product_id)

        Variant.objects.create(product=product, size=size, price=price, stock=stock)
        messages.success(request, "Size variant added successfully.")
        return redirect('variant_list', product_id=product_id)

    return redirect('variant_list', product_id=product_id)

def update_variant(request, variant_id):
    variant = get_object_or_404(Variant, id=variant_id)
    size_choices = get_size_choices(variant.product.category.category_name.lower())
    
    if request.method == "POST":
        size = request.POST.get("size", "").strip()
        price = float(request.POST.get("price", "").strip())
        stock = int(request.POST.get("stock", "").strip())

        if not size or not price or not stock:
            messages.error(request, "All fields are required.")
            return redirect('update_variant', variant_id=variant_id)
        
        if price < 0:
            messages.error(request, 'Price must be a positive indeger')
            return redirect('update_variant', variant_id=variant_id)
        
        if stock < 0:
            messages.error(request, 'Stock must be a positive indeger')
            return redirect('update_variant', variant_id=variant_id)

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messages.error(request, "Price and stock must be valid numbers.")
            return redirect('update_variant', variant_id=variant_id)

        variant.size = size
        variant.price = price
        variant.stock = stock
        variant.save()
        messages.success(request, "Variant updated successfully.")
        return redirect('variant_list', product_id=variant.product.id)

    return render(request, 'admin/variant_update.html', {'variant': variant, 'size_choices': size_choices})


#=======================================================================================================================================

def user_products(request):
    username = request.user.username
    category = request.GET.get('category', 'All') 
    sort_by = request.GET.get('sort_by', 'default') 
    page_number = request.GET.get('page',1)
    search_query = request.GET.get('search', '')

    if search_query:
        product_list = Product.objects.filter(product_name__icontains=search_query)
    elif category == 'All':
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(category__category_name=category)

    if sort_by == 'price_low_high':
        product_list = product_list.order_by('price')
    elif sort_by == 'price_high_low':
        product_list = product_list.order_by('-price')
    elif sort_by == 'discount':
        product_list = product_list.order_by('-offer')
    
    paginator = Paginator(product_list,2)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return render(request, 'user/shop.html', {
        'products': products,
        'username': username,
        'selected_category': category,
        'selected_sort': sort_by,
    })

#=======================================================================================================================================





def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_listed=True)
    variants = product.variants.all()
    

    for variant in variants:
        variant.highest_offer = max(
            variant.offer_percentage,
            variant.product.offer_percentage,
            variant.product.category.category_offer)
        
    context = {
        'product': product,
        'variants': variants,
        'offer': variant.highest_offer,
    }
    return render(request, 'user/product-detail.html', context)




#=======================================================================================================================================