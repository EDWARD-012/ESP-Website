import unittest

from esp.users.forms import EmailUserRegForm, UserRegForm, SinglePhaseUserRegForm

class TestEmailFieldValidation(unittest.TestCase):

    def test_email_user_reg_form_requires_email(self):
        form = EmailUserRegForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_user_reg_form_requires_email(self):
        form = UserRegForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_single_phase_user_reg_form_requires_email(self):
        form = SinglePhaseUserRegForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_forms_reject_empty_email(self):
        forms = [EmailUserRegForm(data={'email': ''}), UserRegForm(data={'email': ' '}), SinglePhaseUserRegForm(data={'email': ' '})]
        for form in forms:
            self.assertFalse(form.is_valid())
            self.assertIn('email', form.errors)

    def test_forms_accept_valid_email(self):
        valid_emails = ['test@example.com', 'user.name@domain.co', 'user+name@domain.com']
        forms = [EmailUserRegForm(data={'email': email}) for email in valid_emails] + [UserRegForm(data={'email': email}) for email in valid_emails] + [SinglePhaseUserRegForm(data={'email': email}) for email in valid_emails]
        for form in forms:
            self.assertTrue(form.is_valid())

if __name__ == '__main__':
    unittest.main()