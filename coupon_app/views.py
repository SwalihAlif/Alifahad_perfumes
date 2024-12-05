from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Coupon

#------------------------------ check if user is admin ----------------------------------------------
def is_admin(user):
    return user.is_superuser

#------------------------------ admin coupon list ----------------------------------------------
@user_passes_test(is_admin)
def coupon_list(request):
    coupons = Coupon.objects.all()
    return render(request, 'admin/coupon_list.html', {'coupons': coupons})
#------------------------------ admin coupon add ----------------------------------------------
@user_passes_test(is_admin)
def coupon_add(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        discount_amount = request.POST.get('discount_amount')
        discount_type = request.POST.get('discount_type')
        valid_until = request.POST.get('valid_until')
        active = request.POST.get('active') == 'on'  


        Coupon.objects.create(
            code = code,
            discount_amount = discount_amount,
            discount_type = discount_type,
            valid_until = valid_until,
            active = active
        )
        messages.success(request, 'Coupon added successfully.')
        return redirect('coupon_list')
    return render(request, 'admin/coupon_form.html')

#------------------------------ admin coupon edit ----------------------------------------------
@user_passes_test(is_admin)
def coupon_edit(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    if request.method == 'POST':
        coupon.code = request.POST.get('code')
        coupon.discount_amount = request.POST.get('discount_amount')
        coupon.discount_type = request.POST.get('discount_type')
        coupon.valid_until = request.POST.get('valid_until')
        coupon.active = request.POST.get('active') == 'on'
        coupon.save()
        messages.success(request, 'Coupon updated successfully.')
        return redirect('coupon_list')
    return render(request, 'admin/coupon_form.html', {'coupon': coupon})

#------------------------------ admin coupon delete ----------------------------------------------
@user_passes_test(is_admin)
def coupon_delete(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    coupon.delete()
    messages.success(request, 'Coupon deleted successfully.')
    return redirect('coupon_list')
#------------------------------ admin coupon management ----------------------------------------------
#------------------------------ admin coupon management ----------------------------------------------

# @login_required
# def checkout(request):
#     user = request.user
#     try:
#         cart = Cart.objects.get(user_id=user)
#         items = CartItem.objects.filter(cart=cart)
        
#         for item in items:
#             item.total_price = item.variant.price * item.quantity
#             item.save()

#         grand_total = sum(item.total_price for item in items)
#         shipping_charge = 0 if grand_total > 1000 else 150
#         sub_total = grand_total + shipping_charge

#         coupon_discount = 0
#         if cart.coupon and cart.coupon_active:
#             if cart.coupon.discount_type == 'percentage':
#                 coupon_discount = (cart.coupon.discount_amount / 100) * grand_total
#             elif cart.coupon.discount_type == 'fixed':
#                 coupon_discount = cart.coupon.discount_amount

#         grand_total -= coupon_discount

#         # Create the order
#         order = Order.objects.create(
#             user_id=user,
#             address=user.userprofile,  # Assuming there's a user profile relation
#             payment_method="COD",
#             coupon_name=cart.coupon.code if cart.coupon else '',
#             coupon_discount=coupon_discount,
#             total_amount=grand_total,
#         )

#         # Add order items
#         for item in items:
#             OrderItems.objects.create(
#                 order=order,
#                 product_added=item.variant,
#                 quantity=item.quantity,
#                 size=item.variant.size,
#                 final_product_price=item.variant.price * item.quantity
#             )
#             item.delete()  # Remove item from cart

#         # Clear cart
#         cart.coupon = None
#         cart.coupon_active = False
#         cart.save()

#         messages.success(request, "Order placed successfully.")
#         return redirect('order_success')

#     except Cart.DoesNotExist:
#         messages.error(request, "Cart not found.")
#         return redirect('cart_show')

