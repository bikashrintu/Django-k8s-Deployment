from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import NewStock,AddStock,Review

def home(request):
    """Display all products on the homepage."""
    new_stocks = NewStock.objects.all()  # Fetch all stock data
    added_stock=AddStock.objects.all().order_by('-id')
    reviews = Review.objects.all()  # Fetch all reviews from the database
    return render(request,'index.html',{'added_stock':added_stock,'new_stocks': new_stocks,'reviews': reviews})



from django.shortcuts import redirect

def review(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        city = request.POST.get('city', '').strip()
        review_text = request.POST.get('review', '').strip()
        image = request.FILES.get('image')  # Handle file upload

        if not name or not city or not review_text:
            return HttpResponse("All fields are required!", status=400)

        # Save review with image
        Review.objects.create(name=name, city=city, review=review_text, image=image)
        
        return redirect('home')  # Redirect to home after submission

    return render(request, 'review.html')


# def display_reviews(request):
#     reviews = Review.objects.all()  # Fetch all reviews from the database
#     return render(request, 'index.html', {'reviews': reviews})
# def display_reviews(request):
#     reviews = Review.objects.all()  # Fetch all reviews from the database
#     return render(request, 'reviews.html', {'reviews': reviews})  # Use a separate template





def product_details(request, car_id):
    car = get_object_or_404(AddStock, id=car_id)
    car_images = car.images.all()
    similar_cars = AddStock.objects.filter(type=car.type).exclude(id=car.id)[:]
    # added_stock = AddStock.objects.all()

    return render(request, 'product_details.html', {
        'car': car,
        'car_images': car_images,
        'similar_cars': similar_cars,
        # 'added_stock': added_stock
    })





# Create your views here.
