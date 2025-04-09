from django.shortcuts import render
from .models import Dish, Review
from .forms import BookingForm, ReviewForm

def menu_view(request):
    dishes = Dish.objects.all()
    return render(request, 'cafe/menu.html', {'dishes': dishes})

def home_view(request):
    return render(request, 'cafe/home.html')

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cafe/booking_success.html')
    else:
        form = BookingForm()
    return render(request, 'cafe/booking.html', {'form': form})


def reviews_view(request):
    reviews = Review.objects.order_by('-created_at')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    return render(request, 'cafe/reviews.html', {'form': form, 'reviews': reviews})
