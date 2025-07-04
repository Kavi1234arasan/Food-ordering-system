from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem, Customer, Order

# Home page – List food items
def home(request):
    items = FoodItem.objects.all()
    return render(request, 'home.html', {'datas': items})


# Add new food item
def addData(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        restaurant = request.POST['restaurants']
        rating = request.POST['ratings']

        if name and price and restaurant and rating:
            FoodItem.objects.create(
                name=name,
                price=float(price),
                restaurant=restaurant,
                rating=float(rating)
            )
        return redirect('home')
    return redirect('home')


# Update existing food item
def updateData(request, id):
    food_item = get_object_or_404(FoodItem, id=id)

    if request.method == 'POST':
        food_item.name = request.POST.get('name')
        food_item.price = request.POST.get('price')
        food_item.restaurant = request.POST.get('restaurants')
        food_item.rating = request.POST.get('ratings')
        food_item.save()
        return redirect('home')

    return render(request, 'update.html', {'data': food_item})


# Delete a food item
def deleteData(request, id):
    food_item = get_object_or_404(FoodItem, id=id)
    food_item.delete()
    return redirect('home')


# Place a food order
def place_order(request):
    items = FoodItem.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        food_id = request.POST.get('food_item')
        quantity = request.POST.get('quantity')

        if name and email and address and food_id and quantity:
            customer = Customer.objects.create(name=name, email=email, address=address)
            food = get_object_or_404(FoodItem, id=food_id)
            Order.objects.create(customer=customer, food_item=food, quantity=int(quantity))
            return redirect('order_success')

    return render(request, 'place_order.html', {'items': items})


# Display all orders
def order_success(request):
    orders = Order.objects.select_related('customer', 'food_item').order_by('-order_date')
    return render(request, 'order_success.html', {'orders': orders})
