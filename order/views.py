from django.views.generic.edit import CreateView

from order.forms import OrderForm
from order.signals import order_notifying


class CreateOrderView(CreateView):
    form_class = OrderForm
    template_name = 'order/order_create.html'

    def get_success_url(self):
        return '/success/'

    def form_valid(self, form):
        result = super(CreateOrderView, self).form_valid(form)
        order_notifying(self.object)
        return result
