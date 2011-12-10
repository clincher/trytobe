from django.conf.urls.defaults import patterns, url

from order.views import CreateOrderView


urlpatterns = patterns('',
    # Products
    url(r'^create$',
        CreateOrderView.as_view(),
        name='order_create'
    ),
)