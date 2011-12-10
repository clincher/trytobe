from forms import OrderForm


def order_form(request):
    order_form = OrderForm(request.POST or {})
    return {'form': order_form}
  