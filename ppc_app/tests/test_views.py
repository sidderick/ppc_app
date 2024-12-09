from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ppc_app.models import PersonDetails


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.superuser = User.objects.create_superuser(username='admin', password='adminpassword')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppc_app/index.html')

    def test_person_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppc_app/person_list.html')

    def test_person_list_view_unauthenticated(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppc_app/index.html')

    def test_register_user_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_person_create_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('person_create'), {
            'nhsNumber': '1234567890',
            'firstName': 'John',
            'surname': 'Doe',
            'dateOfBirth': '1990-01-01',
            'email': 'john.doe@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(PersonDetails.objects.filter(nhsNumber='1234567890').exists())

    def test_person_delete_view_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        person = PersonDetails.objects.create(
            nhsNumber='1234567890',
            firstName='Jane',
            surname='Doe',
            dateOfBirth='1995-01-01',
            email='jane.doe@example.com',
        )
        response = self.client.post(reverse('person_delete', args=[person.userID]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(PersonDetails.objects.filter(nhsNumber='1234567890').exists())
