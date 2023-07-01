from .basket import Basket


def basket(request):
    basket_instance = Basket(request)

    return {'basket': basket_instance}
