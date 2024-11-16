from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Note: All test user passwords are "testpass1234"


class UsersManagersTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            password="testpass1234",
            age=22,
            weight=150,
            fitness_level=3,
            gender=2,
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.age, 22)
        self.assertEqual(user.weight, 150)
        self.assertEqual(user.fitness_level, 3)
        self.assertEqual(user.gender, 2)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
            age=50,
            fitness_level=2,
            gender=1,
        )

        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertEqual(admin_user.age, 50)
        self.assertEqual(admin_user.fitness_level, 2)
        self.assertEqual(admin_user.gender, 1)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "first_name": "Test",
                "last_name": "User",
                "age": "22",
                "weight": "150",
                "fitness_level": "3",
                "gender": "2",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")
        self.assertEqual(get_user_model().objects.all()[0].first_name, "Test")
        self.assertEqual(get_user_model().objects.all()[0].last_name, "User")
        self.assertEqual(get_user_model().objects.all()[0].age, 22)
        self.assertEqual(get_user_model().objects.all()[0].weight, 150)
        self.assertEqual(get_user_model().objects.all()[0].fitness_level, 3)
        self.assertEqual(get_user_model().objects.all()[0].gender, 2)
