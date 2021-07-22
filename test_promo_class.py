from datetime import datetime
from Promo_class import Promo
import inspect


NOW =  datetime.now()


def test_promo_expired():
    past_time = NOW - timedelta(seconds = 3)
    promo = Promo('Python ejercicio', past_time)
    assert promo.expired


def test_promo_not_expired():
    future_time = NOW + timedelta(days = 1)
    promo = Promo('Python IDE', future_time)
    assert not promo.expired

def test_uses_property():
    assert 'property' in inspect.getsource(Promo)
