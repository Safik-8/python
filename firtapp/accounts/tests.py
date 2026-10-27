from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse


class AuthenticationViewTests(TestCase):
    def test_register_login_and_logout(self):
        response = self.client.post(
            reverse('accounts:register'),
            {
                'username': 'ada',
                'email': 'ada@example.com',
                'password1': 'ComplexPass123',
                'password2': 'ComplexPass123',
            },
        )
        self.assertRedirects(response, reverse('accounts:profile'))
        self.assertTrue(User.objects.filter(username='ada').exists())

        self.client.post(reverse('accounts:logout'))
        response = self.client.post(
            reverse('accounts:login'),
            {'username': 'ada', 'password': 'ComplexPass123'},
        )
        self.assertRedirects(response, reverse('accounts:profile'))

    def test_password_reset_uses_builtin_flow(self):
        User.objects.create_user('grace', 'grace@example.com', 'ComplexPass123')

        response = self.client.post(reverse('accounts:password_reset'), {'email': 'grace@example.com'})
        self.assertRedirects(response, reverse('accounts:password_reset_done'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('/accounts/reset/', mail.outbox[0].body)
