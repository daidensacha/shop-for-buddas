from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product


def profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    # Order context creation
    # try:
    #     orders = Order.objects.filter(user_profile__user=request.user)
    #     print(orders)
    # Linting error, do not use bare except - fix
    # except:
    #     orders = None

    # products context
    try:
        products = Product.objects.filter(created_by=request.user)
    # Linting error, do not use bare except - fix
    except:
        products = None

    # vendor orders
    vendor_order_list = []
    if products != None:
        for product in products:
            vendor_orders = OrderLineItem.objects.filter(product=product)
            vendor_order_list.append(vendor_orders)

    

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance= profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()
            messages.success(request, 'Profile updated successfully')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'products': products,
        'on_profile_page': True,
        'vendor_order_list': vendor_order_list,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

    
def UserProfileUpdate(request):
    profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()

    context = {
        'form': form,
    }
    return redirect(request, "profiles/profile.html", context)