# customuser/tests.py
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse, resolve

from .views import MyLoginView, usersignup



class CustomUserTests(TestCase):


    def test_create_user(self):
        myCustomUser = get_user_model()
        user = myCustomUser.objects.create_user(
            email='testguy@example.com',
            password='M5Nh32AZNxrMojNcRoAb',
            first_name='testguy',
            last_name='myman'
        )
        self.assertEqual(user.email, 'testguy@example.com')
        self.assertEqual(user.first_name, 'testguy')
        self.assertEqual(user.last_name, 'myman')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        myCustomUser = get_user_model()
        admin_user = myCustomUser.objects.create_superuser(
            email='testsuperguy@example.com',
            password='M5Nh32AZNxrMojNcRoAb',
            first_name='testsuperguy',
            last_name='mydude'
        )
        self.assertEqual(admin_user.email, 'testsuperguy@example.com')
        self.assertEqual(admin_user.first_name, 'testsuperguy')
        self.assertEqual(admin_user.last_name, 'mydude')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_admin)



class LoginPageTests(TestCase):


    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)
        myCustomUser = get_user_model()
        user = myCustomUser.objects.create_user(
            email='testguy@example.com',
            password='M5Nh32AZNxrMojNcRoAb',
            first_name='testguy',
            last_name='myman',
        )
        user = get_user_model().objects.get(email='testguy@example.com')
        user.is_active = True
        user.save()


    def test_loginpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_loginpage_template(self):
        self.assertTemplateUsed(self.response, 'registration/login.html')

    def test_loginpage_contains_correct_html(self):
        self.assertContains(self.response, 'Log In')

    def test_loginpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Silly text like collywobbles.')

    def test_loginpage_url_resolves_myloginview(self):
        view = resolve('/accounts/login/')
        self.assertEqual(
            view.func.__name__,
            MyLoginView.as_view().__name__
        )

    def test_loginform_logs_user_in(self):
        url = reverse('login')
        self.response = self.client.post(
            url, data={
                "username": "testguy@example.com",
                "password": "M5Nh32AZNxrMojNcRoAb"
            }
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['user'].email, 'testguy@example.com')

    def test_loginform_redirects_home(self):
        url = reverse('login')
        self.response = self.client.post(
            url, data={
                "username": "testguy@example.com",
                "password": "M5Nh32AZNxrMojNcRoAb"
            }
        )
        self.assertRedirects(self.response, reverse('home'))



class SignupPageTests(TestCase):


    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signuppage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signuppage_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signuppage_contains_correct_html(self):
        self.assertContains(self.response, 'Sign up')

    def test_signuppage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Silly text like collywobbles.')

    def test_signuppage_url_resolves_usersignup(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            usersignup.__name__
        )

    def test_signupform_creates_user(self):
        url = reverse('signup')
        self.response = self.client.post(
            url, data={
                'email':'testguy@example.com',
                'password1':'M5Nh32AZNxrMojNcRoAb',
                'password2':'M5Nh32AZNxrMojNcRoAb',
                'first_name':'testguy',
                'last_name':'myman'
            }
        )
        savedemail = get_user_model().objects.get(email__iexact='testguy@example.com').email
        self.assertEqual(savedemail, 'testguy@example.com')

    def test_signupform_renders_confirmation_prompt(self):
        url = reverse('signup')
        self.response = self.client.post(
            url, data={
                'email':'testguy@example.com',
                'password1':'M5Nh32AZNxrMojNcRoAb',
                'password2':'M5Nh32AZNxrMojNcRoAb',
                'first_name':'testguy',
                'last_name':'myman'
            }
        )
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/please_confirm.html')


    def test_signupform_sends_email(self):
        url = reverse('signup')
        self.response = self.client.post(
            url, data={
                'email':'testguy@example.com',
                'password1':'M5Nh32AZNxrMojNcRoAb',
                'password2':'M5Nh32AZNxrMojNcRoAb',
                'first_name':'testguy',
                'last_name':'myman'
            }
        )
        self.assertTemplateUsed(self.response, 'registration/activate_account.html')
        self.assertEqual(len(mail.outbox), 1)