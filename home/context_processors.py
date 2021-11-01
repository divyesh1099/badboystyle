from product.models import Type
from offer.models import Offer

def get_categories(request):
    categories = Type.objects.all()
    return {
        'categories': categories,
    }

def get_offers(request):
    offers = Offer.objects.all()
    return {
        'offers': offers,
    }