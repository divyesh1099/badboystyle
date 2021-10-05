from product.models import Type
def get_categories(request):
    categories = Type.objects.all()
    return {
        'categories': categories,
    }