## Testing initial session variables stored in cookies

This is example project which shows you how to test cookie-session variables. Whole
repository is made as a minimal working example. Please take a look into `tests.py`
file and find how we assign initial session variable before requests. For better
understanding, see also the view in `views.py` and routing in `urls.py`

### Key points
1. We use session variables stored in cookies. See the entry in `settings.py`:

`SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"`

2. If you want to assume previously set session variable, remember to reassign it to
the cookie after modification, as in `tests.py`:

```python
session = self.client.session
session["foo"] = DUMMY_INT
session.save()

# Update session's cookie
session_cookie_name = django_settings.SESSION_COOKIE_NAME
self.client.cookies[session_cookie_name] = session.session_key
```

### How to run
* clone the repository
* create `venv` with Python 3.7.6 and activate
* `$ pip install -r requirements.txt`
* `$ cd test_session_variables`
* `$ ./manage.py test`