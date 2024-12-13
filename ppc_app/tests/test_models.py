from django.test import TestCase
from ppc_app.models import PersonDetails, CertificateDetails


class PersonDetailsModelTestCase(TestCase):
    def setUp(self):
        """Set up initial data for testing."""
        self.person = PersonDetails.objects.create(
            nhsNumber='1234567890',
            firstName='John',
            surname='Doe',
            dateOfBirth='1980-01-01',
            email='johndoe@example.com'
        )

    def test_person_creation(self):
        """Test that a PersonDetails object is created correctly."""
        self.assertEqual(self.person.nhsNumber, '1234567890')
        self.assertEqual(self.person.firstName, 'John')
        self.assertEqual(self.person.surname, 'Doe')
        self.assertEqual(self.person.dateOfBirth, '')
        self.assertEqual(self.person.email, 'johndoe@example.com')
        self.assertIsInstance(self.person, PersonDetails)

    def test_person_string_representation(self):
        """Test the string representation of the PersonDetails object."""
        self.assertEqual(str(self.person), str(self.person.userID))

    def test_person_update(self):
        """Test updating a PersonDetails object."""
        self.person.firstName = 'Jane'
        self.person.surname = 'Smith'
        self.person.save()
        updated_person = PersonDetails.objects.get(userID=self.person.userID)
        self.assertEqual(updated_person.firstName, 'Jane')
        self.assertEqual(updated_person.surname, 'Smith')

    def test_person_delete(self):
        """Test deleting a PersonDetails object."""
        user_id = self.person.userID
        self.person.delete()
        with self.assertRaises(PersonDetails.DoesNotExist):
            PersonDetails.objects.get(userID=user_id)
