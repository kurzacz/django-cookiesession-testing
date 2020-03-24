from django.conf import settings as django_settings
from django.test import TestCase
from django.urls import reverse


class FooTestCase(TestCase):

    def test_foo(self):
        """Verify if view returns session variable and increase by one."""

        # GIVEN
        DUMMY_INT = 2

        session = self.client.session
        session["foo"] = DUMMY_INT
        session.save()

        # Update session's cookie
        session_cookie_name = django_settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie_name] = session.session_key

        # WHEN
        response = self.client.get(reverse("example_view"))

        # THEN
        assert bytes.decode(response.content, 'utf8') == str(DUMMY_INT)
        assert self.client.session["foo"] == DUMMY_INT+1
