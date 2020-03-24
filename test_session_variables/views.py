from django.http import HttpResponse


def view_session_variable(request):
    session_value = request.session['foo']
    request.session['foo'] += 1
    return HttpResponse(session_value)
