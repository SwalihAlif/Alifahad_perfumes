from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from product_app.models import Product
from .models import Rating, Review


# Create your views here.

@csrf_exempt
@login_required
def submit_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get('product_id')
        rating = data.get('rating')
        title = data.get('title')
        comment =data.get('comment')

        try:
            product = Product.objects.get(id=product_id)
            user = request.user

            rating_obj = Rating.objects.create(
                product=product,
                user=user,
                score=rating
            )

            review_obj = Review.objects.create(
                product=product,
                user=user,
                title=title,
                content=comment
            )

            response = {
                'status': 'success',
                'message': 'Review submitted successfully!'
            }

            return JsonResponse(response, status=200)
        
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)



#-------------------------- admin side review -----------------------------------------------------------------------
from django.shortcuts import render
from .models import Rating, Review

def ratings_and_reviews_admin(request):
    ratings = Rating.objects.select_related('user', 'product').all()
    reviews = Review.objects.select_related('user', 'product', 'rating').all()

    context = {
        'ratings': ratings,
        'reviews': reviews,
    }
    return render(request, 'admin/custom_ratings_reviews.html', context)
