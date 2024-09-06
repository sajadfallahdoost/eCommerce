from django.db import models
from shop.models.cart import Cart
from shop.models.order import Order
from shop.models.order_address import OrderAddress
from shop.models.cart_item import CartItem
from django.core.exceptions import ValidationError
from warehouse.models.pack import Pack
from django.utils.crypto import get_random_string
from decimal import Decimal

'''
from shop.models.coupon import CouponModel
'''


class BasketDataAccessLayer(models.Manager):
    def get_cart(self, user_id):
        return self.filter(user_id=user_id).first()

    def get_cart_items(cart_id):
        return CartItem.objects.filter(cart_id=cart_id)

    def get_order(user_id, transaction_number):
        return Order.objects.filter(user_id=user_id, transaction_number=transaction_number).first()

    def get_orders_by_user(user_id):
        return Order.objects.filter(user_id=user_id)

    def get_orders_by_status(status):
        return Order.objects.filter(status=status)

    def get_order_addresses(user_id):
        return OrderAddress.objects.filter(user_id=user_id)

    def get_user_orders(user_id):
        return Order.objects.filter(user_id=user_id)

    def get_order_details(order_id):
        return Order.objects.get(id=order_id)


class BasketBusinessLogicLayer(models.Manager):
    """
    Handles functions affecting the user's basket and orders.
    """

    def add_to_cart(self, user, pack_id, quantity):
        cart, created = Cart.objects.get_or_create(user=user)
        pack = Pack.objects.get(id=pack_id)

        if not pack.is_active:
            raise ValidationError("This pack is not available for purchase.")

        cart_item, created = CartItem.objects.get_or_create(cart=cart, pack=pack, defaults={'quantity': quantity})

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item
    
    # applying coupon check 
    '''
    def apply_coupon(self, coupon, order, user, total_price):
    def apply_coupon(self, coupon, order, user, total_price):
        if coupon:
            # discount_amount = round(
            #     (total_price * Decimal(coupon.discount_percent / 100)))
            # total_price -= discount_amount ====> calculating final price with discount

            order.coupon = coupon
            coupon.used_by.add(user)
            coupon.save()
    '''
    def remove_from_cart(self, user, cart_item_id):
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        cart_item.delete()

    def calculate_cart_total(self, cart):
        total = Decimal(0)
        for item in cart.items.all():
            total += item.pack.price * item.quantity
        return total

    def create_order_from_cart(self, user, order_address_data):
        cart = Cart.objects.get(user=user)
        if not cart.items.exists():
            raise ValidationError("The cart is empty.")

        total_price = self.calculate_cart_total(cart)
        transaction_number = get_random_string(12).upper()

        order_address = OrderAddress.objects.create(**order_address_data)

        order = Order.objects.create(
            user=user,
            transaction_number=transaction_number,
            total_price=total_price,
            status='submitted',
            order_address=order_address,
            cart=cart
        )

        cart.items.all().delete()
        
        return order

    def update_order_status(self, order_id, status):
        order = Order.objects.get(id=order_id)
        order.status = status
        order.save()
        return order

# this class check our coupon in user basket is valid or not 
'''
class ValidateCouponView(LoginRequiredMixin, HasCustomerAccessPermission, View):

    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        user = self.request.user

        status_code = 200
        message = "کد تخفیف با موفقیت ثبت شد"
        total_price = 0
        total_tax = 0

        try:
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            return JsonResponse({"message": "کد تخفیف یافت نشد"}, status=404)
        else:
            if coupon.used_by.count() >= coupon.max_limit_usage:
                status_code, message = 403, "محدودیت در تعداد استفاده"

            elif coupon.expiration_date and coupon.expiration_date < timezone.now():
                status_code, message = 403, "کد تخفیف منقضی شده است"

            elif user in coupon.used_by.all():
                status_code, message = 403, "این کد تخفیف قبلا توسط شما استفاده شده است"

            else:
                cart = CartModel.objects.get(user=self.request.user)

                total_price = cart.calculate_total_price()
                total_price = round(
                    total_price - (total_price * (coupon.discount_percent/100)))
                total_tax = round((total_price * 9)/100)
        return JsonResponse({"message": message, "total_tax": total_tax, "total_price": total_price}, status=status_code)
'''
