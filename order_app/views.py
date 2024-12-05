from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order_app.models import Order, OrderItems, Cancelled_order
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.admin.views.decorators import staff_member_required

#------------------------ Order success ---------------------------------------------------------------------


@login_required(login_url='login')
def order_success(request):
    try:
        # Fetch the last order placed by the user
        last_order = Order.objects.filter(user_id=request.user).last()
        
        if not last_order:
            messages.error(request, "No recent orders found.")
            return redirect('home')  # Redirect to home if no order exists
        
        # Render the success page with the last order details
        return render(request, 'user/order_success.html', {
            'last_order': last_order,
        })
    
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')  # In case of error, redirect to home


    
#---------------------------- all orders user side ------------------------------------------------------------------

@login_required(login_url='login')
def all_orders(request):
    try:
        orders = Order.objects.filter(user_id=request.user.id).order_by('-order_date')
        
        paginator = Paginator(orders, 10)  
        
        # Get the current page number from the query parameters
        page_number = request.GET.get('page')
        
        try:
            paginated_orders = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            paginated_orders = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver the last page
            paginated_orders = paginator.page(paginator.num_pages)
        
        return render(request, 'user/all_orders.html', {
            'orders': paginated_orders,
        })
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')


    

#---------------------------- Order details ------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404
from .models import Order

@login_required(login_url='login')
def order_detail(request, serial_number):
    order = get_object_or_404(Order, serial_number=serial_number, user_id=request.user)
    order_item = OrderItems.objects.filter(order=order)
    return render(request, 'user/order_detail.html', {'order': order, 'order_item': order_item})


#---------------------------- Cancel order ------------------------------------------------------------------

@login_required(login_url='login')
def cancel_order(request, order_id):
    try:
        order = get_object_or_404(Order, user_id=request.user, serial_number=order_id)

        order_items = OrderItems.objects.filter(order=order)
        for item in order_items:
            if item.status == "Order Pending":
                item.status = 'Cancelled'
                item.save()

                Cancelled_order.objects.create(
                    ordered_item=item,
                    user=request.user,
                    reason=request.POST.get('reason', 'No reason provided')
                )
        
        # Update order status if all items are cancelled
        if all(item.status == 'Cancelled' for item in order_items):
            order.status = 'Cancelled'
            order.save()

        messages.success(request, "Your order has been cancelled.")
        return redirect('order:all_orders')

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('order:all_orders')

#--------------------------- Admin order management ---------------------------------------------------------------


@staff_member_required
def order_management(request):

    orders_list = Order.objects.prefetch_related('order_all').order_by('-order_date')
    for order in orders_list:
        for item in order.order_all.all():
            if item.status == 'Delivered':
                item.payment_status = 'completed'
            else:
                item.payment_status = 'pending'

            item.save()

    paginator = Paginator(orders_list, 6)
    page_number = request.GET.get('page')
    page_orders = paginator.get_page(page_number)

    context = {
        'orders': page_orders
    }
    return render(request, 'admin/order_management.html', context)

#--------------------------- Admin order details view -------------------------------------------------------------

def order_detail_view(request, order_serial_number):
    # Fetch the order using serial_number
    order = get_object_or_404(Order, serial_number=order_serial_number)
    # Get all items in the order
    order_items = OrderItems.objects.filter(order=order)
    # Fetch user's address
    address = order.address
    
    # Context to pass to the template
    context = {
        "order": order,
        "order_items": order_items,
        "address": address,
    }
    
    return render(request, 'admin/order_detail.html', context)


#------------------------------ admin order status update ----------------------------------------------------------

def change_order_status(request, oid):
    order_item = OrderItems.objects.get(id=oid)

    if request.method == 'POST':
        status = request.POST.get('status')
        order_item.status = status
        order_id = order_item.order
        order_item.save()
        messages.success(request, f"Order status changed to {status}")
        print(f"this is {order_item}")

    return redirect('order:order_detail_view', order_id)
