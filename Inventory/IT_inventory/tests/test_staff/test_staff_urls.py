from django.test import SimpleTestCase
from django.urls import reverse, resolve
from staff.views import greet,dashboard,item,checkoutView,Orders,request_noView,signup,login


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        # assert 1==2
        url = reverse('greet')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,greet)
    def dashboard(self):
        # assert 1==1
        url = reverse('dashboard_staff')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,dashboard)
    def test_item(self):
        # assert 1==2
        url = reverse('items_staff')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,item)
    def test_checkoutView(self):
        # assert 1==2
        url = reverse('checkoutt_staff')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,checkoutView)
    def test_Orders(self):
        # assert 1==2
        url = reverse('requests_staff')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,Orders)
    def test_request_noView(self):
        # assert 1==2
        url = reverse('requests_no_staff')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,request_noView)
    def test_signup(self):
        # assert 1==2
        url = reverse('signup')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,signup)
    def test_login(self):
        # assert 1==2
        url = reverse('login')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,login)