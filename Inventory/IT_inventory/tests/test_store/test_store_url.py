from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import dashboardView,Checkoutview


class TestUrls(SimpleTestCase):
    def test_dashboardView(self):
        url = reverse('dashboard_store')
        self.assertEquals(resolve(url).func.view_class,dashboardView)
    def test_Checkoutview(self):
        url = reverse('checkoutt_store')
        self.assertEquals(resolve(url).func.view_class,Checkoutview)