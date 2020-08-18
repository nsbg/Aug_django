from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def index(request):
    review_form = ReviewForm()
    return render(request, 'index.html', {'review_form' : review_form})
