from django.test import TestCase, Client
from django.urls import reverse, resolve
from rest_framework import status
from api.views import *
from api.views import *
import json


class TestCompanyViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.company_url = reverse('company')
        self.company_detail_url = reverse("company_detail", args=['1'])
        self.company1 = Company.objects.create(
            name="asd",
            employee_number=2499,
            established=1990
        )

    def test_check(self):
        assert 1 == 1

    def test_company_GET(self):
        response = self.client.get(self.company_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_company_detail_GET(self):
        response = self.client.get(self.company_detail_url)
        company1 = Company.objects.get(id=1)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(company1.name, "asd")
        self.assertEquals(company1, self.company1)

    def test_company_POST(self):
        response = self.client.post(self.company_url, {
            "name": "samsung",
            "employee_number": 25,
            "established": 1678
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Company.objects.get(id=2).name, "samsung")
        self.assertEquals(Company.objects.count(), 2)

    def test_company_DELETE(self):
        response = self.client.delete(self.company_detail_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Company.objects.count(), 0)


class TestUserViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = User.objects.create(
            username="admin",
            password="admin",
            email="aseke@gmail.com"
        )
        self.data = {
            "username": "aseke",
            "password": "admin",
            "email": "jokker@mail.com"
        }

    def test_check(self):
        assert 1 + 1 == 2

    def test_signup(self):
        response = self.client.post(self.signup_url, self.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 2)

    def test_login(self):
        self.client.post(self.signup_url, self.data)
        response = self.client.post(self.login_url, {
            "username": "aseke",
            "password": "admin"
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(User.objects.get(id=2).email, "jokker@mail.com")

    def test_logout(self):
        self.client.post(self.signup_url, self.data)
        response1 = self.client.post(self.login_url, {
            "username": "aseke",
            "password": "admin"
        })
        token = response1.data['token']
        token = "Token {}".format(token)
        response2 = self.client.post(self.logout_url, HTTP_AUTHORIZATION=token)
        self.assertEquals(response2.status_code, status.HTTP_204_NO_CONTENT)


class TestReviewViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.review_url = reverse('review')
        self.review_detail_url = reverse("review_info", args=['1'])
        self.review_detail_url2 = reverse("review_info", args=['2'])
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.data = {
            "username": "aseke",
            "password": "admin",
            "email": "jokker@mail.com"
        }
        self.client.post(self.signup_url, self.data)
        response1 = self.client.post(self.login_url, {
            "username": "aseke",
            "password": "admin"
        })
        self.company = Company.objects.create(
            name="apple",
            employee_number=2499909,
            established=1990
        )
        token = response1.data['token']
        self.token = "Token {}".format(token)
        self.review_info = {
            "rating": 1,
            "title": "not working",
            "summary": "please fix it",
            "company_id": 1
        }

    def test_check(self):
        assert 1 + 1 == 2

    def test_review_CREATE(self):
        for i in range(8):
            response = self.client.post(self.review_url, self.review_info, HTTP_AUTHORIZATION=self.token)
        response2 = self.client.post(self.review_url, {
            "rating": 6,
            "title": "not working",
            "summary": "please fix it",
            "company_id": 1
        }, HTTP_AUTHORIZATION=self.token)
        self.assertEquals(Review.objects.count(), 8)
        self.client.post(self.review_url, self.review_info, HTTP_AUTHORIZATION=self.token)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_DELETE(self):
        for i in range(8):
            self.client.post(self.review_url, self.review_info, HTTP_AUTHORIZATION=self.token)
        self.client.delete(self.review_detail_url, HTTP_AUTHORIZATION=self.token)
        response = self.client.delete(self.review_detail_url2, HTTP_AUTHORIZATION=self.token)
        self.assertEquals(Review.objects.count(), 6)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_GET(self):
        self.client.post(self.review_url, self.review_info, HTTP_AUTHORIZATION=self.token)
        self.client.post(self.review_url, {
            "rating": 5,
            "title": "good working",
            "summary": "very good",
            "company_id": 1
        }, HTTP_AUTHORIZATION=self.token)
        response = self.client.get(self.review_detail_url, HTTP_AUTHORIZATION=self.token)
        response2 = self.client.get(self.review_detail_url2, HTTP_AUTHORIZATION=self.token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response2.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['rating'], 1)
        self.assertEquals(response.data['title'], "not working")
        cmp = vars(Company.objects.get(id=1))
        del cmp['_state']
        self.assertEquals(dict(response2.data['company']), cmp)
