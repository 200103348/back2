from urllib import response
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse, resolve
from .models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser, User
from .views import *

# Create your tests here.
class First(TestCase):
    def test_first(self):
        url=reverse("sportnews")
        self.assertEquals(resolve(url).func,form)

    def test_url_exists(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)
        
        
        
    def test_accessible(self):
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)

    def test_medal(self):
        fullname = Tokyo.objects.create(fullname="Ilya")
        sport = Tokyo.objects.create(sport="First")
        category = Tokyo.objects.create(category='winter')
        medal = Tokyo.objects.create(medal='gold')
        self.assertTrue(str(sport))


    def test_setUp(self):
        response = self.client.get("/olympics/")
        self.assertEqual(response.status_code, 200)