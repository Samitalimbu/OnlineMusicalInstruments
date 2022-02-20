
# Create your tests here.
from Kitab.views import home, Kitab, book_details
from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from django.contrib.auth.models import User,auth
from Kitab.models import Booking, kitab

# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_resolve_to_home(self):

        url = reverse("home")

        resolver = resolve(url)

        self.assertEquals(resolver.func, home)

    def test_resolve_to_AddData(self):

        url = reverse("addData")

        resolver = resolve(url)

        self.assertEquals(resolver.func, Kitab)

    def test_resolve_to_bookDetails(self):

        url = reverse("book_details", args=[1])

        resolver = resolve(url)

        self.assertEquals(resolver.func, book_details)


class TestView(TestCase):

    def test_register_view(self):

        client = Client()
        response = client.get(reverse("register"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'pages/register.html')





    def test_add_product_view(self):

        client = Client()
        logged_in = client.login(username = 'admin',password ='admin')
        response = client.get(reverse("addproduct"))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/adminControl/admin_product.html')




    def test_delete_product_view(self):
        client = Client()
        newProduct=Booking.objects.create(name='shampoo',)
        response = client.delete(reverse("delete-product"),args=[p_id])
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/delete-product/')    




       
 
  
 

