from decimal import Decimal
from django.conf import settings
from shop.models import Yarn


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, yarn, quantity=1, update_quantity=False):
        yarn_id = str(yarn.id)
        if yarn_id not in self.cart:
            self.cart[yarn_id] = {'quantity': 0,
                                  'price': str(yarn.subcat.price)}

        if update_quantity:
            self.cart[yarn_id]['quantity'] = quantity
        else:
            self.cart[yarn_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # save changes in cart
        self.session.modified = True

    def remove(self, yarn):
        yarn_id = str(yarn.id)

        if yarn_id in self.cart:
            del self.cart[yarn_id]
            self.save()

    def __iter__(self):
        yarn_ids = self.cart.keys()
        yarns = Yarn.objects.filter(id__in=yarn_ids)
        for yarn in yarns:
            self.cart[str(yarn.id)]['yarn'] = yarn

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
