from django.test import TestCase
from ppc_app.forms import RegistrationForm, PersonDetailsForm, CertificateDetailsForm
from ppc_app.models import PersonDetails, CertificateDetails


class TestForms(TestCase):
    def test_registration_form_valid(self):
        form = RegistrationForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_password_mismatch(self):
        form = RegistrationForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'differentpassword',
        })
        self.assertFalse(form.is_valid())

    def test_person_details_form_valid(self):
        form = PersonDetailsForm(data={
            'nhsNumber': '1234567890',
            'firstName': 'John',
            'surname': 'Doe',
            'dateOfBirth': '1990-01-01',
            'email': 'john.doe@example.com',
        })
        self.assertTrue(form.is_valid())

    def test_certificate_details_form_valid(self):
        person = PersonDetails.objects.create(
            userID=1000,
            nhsNumber='1234567890',
            firstName='Jane',
            surname='Doe',
            dateOfBirth='1995-01-01',
            email='jane.doe@example.com',
        )
        form = CertificateDetailsForm(data={
            'userID': person.userID,
            'certType': 'ppc',
            'datePurchased': '2023-01-01',
        })
        self.assertTrue(form.is_valid())
