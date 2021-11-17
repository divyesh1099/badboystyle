from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from .models import Review, ReviewImage
from django.shortcuts import redirect

# Create your views here.
@login_required
def index(request, name):
    product = Product.objects.get(name = name)
    review = Review.objects.get_or_create(user = request.user, product = product)[0]
    reviewImages = ReviewImage.objects.filter(review = review)
    # try:
    # except Exception as e:
    #     print("Find Review and ReviewImage error is ", e)
    if request.method == "POST":
        review = Review.objects.get_or_create(user = request.user, product = product)[0]
        reviewImages = ReviewImage.objects.filter(review = review)

        if request.POST["comment"]:
            comment = request.POST["comment"]
            review.comment = comment
            review.save()
        if request.FILES:
            # for image in request.FILES["images"]:
            #     print("Image:", type(image))
            new_images = request.FILES.getlist("images")
            # try:
            #     review_images = ReviewImage.get_or_create(review = review)
            # except Exception as e:
            #     print("Review Error is ", e)
            # print(new_images, "new images")
            if len(new_images) == 1:
                try:
                    # new_review_image = ReviewImage(image = new_images)
                    # print(new_review_image)
                    # review.images.add(ReviewImage.objects.create(image = new_review_image))
                    # review.save()
                    # print(review, "Review ")
                    ReviewImage.objects.create(review = review ,image = new_images[0])
                except Exception as e:
                    print("File upload error is:", e)

            elif len(new_images)>1:
                try:
                    for image in new_images:
                        ReviewImage.objects.create(review = review ,image = image)
                except Exception as e:
                    print("Multiple Files Upload error is", e)
        context = {
            'product':product,
            'review':review,
            'reviewImages':reviewImages
        }
        return render(request, 'review/index.html', context)

    context = {
        'product':product,
        'review':review,
        'reviewImages':reviewImages
    }
    return render(request, 'review/index.html', context)

def delete_review(request, name):
    return redirect('/product/' + str(name))