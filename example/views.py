# Create your views here.
from django.http import HttpResponse
from eventlet.greenthread import sleep
from functools import wraps

def generator_view(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        iterable = func(*args, **kwargs)
        return HttpResponse(iterable)
    return wrapper


@generator_view
def home(request):
    m = "a" * 1000
    for _ in xrange(10):
        yield m
        sleep(0)
