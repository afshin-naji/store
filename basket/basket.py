
from decimal import Decimal
from store.models import Product

class Basket:

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
            
        self.basket = basket

    
    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']

            yield item

    
    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = { 'price': str(product.price), 'qty': qty }

        self.session.modified = True


    def delete(self, product):
        product_id = product

        if product_id in self.basket:
            del self.basket[product_id]

        self.session.modified = True

    
    def __len__(self):

        return sum(item['qty'] for item in self.basket.values())


    def get_total_price(self):
        
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
