from rest_framework.views import APIView
from rest_framework.response import Response
from .service import Cart
from rest_framework import status


class CartList(APIView):

    def get(self, request, format=None):
        cart = Cart(request)
        return Response({'data': list(cart.__iter__()),
                         'cart_total_price': cart.get_total_price()},
                        status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        cart = Cart(request)

        if 'remove' in request.data:
            product = request.data['product']
            cart.remove(product)
        elif 'clear' in request.data:
            cart.clear()
        else:
            cart.add(product=request.data['product'],
                     quantity=request.data['quantity'],
                     update_quantity=request.data['update_quantity'] if 'update_price' in request.data else False)
        return Response({'message': 'cart updated'},
                        status=status.HTTP_200_OK)