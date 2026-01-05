from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Review, AccommodationReview, ActivityReview
from .forms import ReviewForm, AccommodationReviewForm, ActivityReviewForm
from destinations.models import Destination, Accommodation, Activity

@login_required
def add_destination_review(request, destination_slug):
    """Add a review for a destination"""
    destination = get_object_or_404(Destination, slug=destination_slug)

    # Check if user has already reviewed this destination
    if Review.objects.filter(user=request.user, destination=destination).exists():
        messages.info(request, 'You have already reviewed this destination. You can edit your existing review.')
        review = Review.objects.get(user=request.user, destination=destination)
        return redirect('edit_destination_review', destination_slug=destination_slug, review_id=review.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.destination = destination
            review.save()
            messages.success(request, 'Your review has been added successfully.')
            return redirect('destination_detail', slug=destination_slug)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'destination': destination,
        'review_type': 'destination'
    })

@login_required
def edit_destination_review(request, destination_slug, review_id):
    """Edit a destination review"""
    destination = get_object_or_404(Destination, slug=destination_slug)
    review = get_object_or_404(Review, id=review_id, user=request.user, destination=destination)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully.')
            return redirect('destination_detail', slug=destination_slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {
        'form': form,
        'destination': destination,
        'review': review,
        'review_type': 'destination'
    })

@login_required
def delete_destination_review(request, destination_slug, review_id):
    """Delete a destination review"""
    destination = get_object_or_404(Destination, slug=destination_slug)
    review = get_object_or_404(Review, id=review_id, user=request.user, destination=destination)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect('destination_detail', slug=destination_slug)

    return render(request, 'reviews/delete_review.html', {
        'destination': destination,
        'review': review,
        'review_type': 'destination'
    })

@login_required
def add_accommodation_review(request, accommodation_id):
    """Add a review for an accommodation"""
    accommodation = get_object_or_404(Accommodation, id=accommodation_id)

    # Check if user has already reviewed this accommodation
    if AccommodationReview.objects.filter(user=request.user, accommodation=accommodation).exists():
        messages.info(request, 'You have already reviewed this accommodation.')
        return redirect('accommodation_detail', pk=accommodation_id)

    if request.method == 'POST':
        form = AccommodationReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.accommodation = accommodation
            review.save()
            messages.success(request, 'Your review has been added successfully.')
            return redirect('accommodation_detail', pk=accommodation_id)
    else:
        form = AccommodationReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'accommodation': accommodation,
        'review_type': 'accommodation'
    })

@login_required
def add_activity_review(request, activity_id):
    """Add a review for an activity"""
    activity = get_object_or_404(Activity, id=activity_id)

    # Check if user has already reviewed this activity
    if ActivityReview.objects.filter(user=request.user, activity=activity).exists():
        messages.info(request, 'You have already reviewed this activity.')
        return redirect('activity_detail', pk=activity_id)

    if request.method == 'POST':
        form = ActivityReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.activity = activity
            review.save()
            messages.success(request, 'Your review has been added successfully.')
            return redirect('activity_detail', pk=activity_id)
    else:
        form = ActivityReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'activity': activity,
        'review_type': 'activity'
    })

@login_required
def my_reviews(request):
    """View for listing user's reviews"""
    destination_reviews = Review.objects.select_related('destination').filter(user=request.user)
    accommodation_reviews = AccommodationReview.objects.select_related('accommodation').filter(user=request.user)
    activity_reviews = ActivityReview.objects.select_related('activity').filter(user=request.user)

    return render(request, 'reviews/my_reviews.html', {
        'destination_reviews': destination_reviews,
        'accommodation_reviews': accommodation_reviews,
        'activity_reviews': activity_reviews
    })
