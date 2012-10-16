# Create your views here.
from decimal import getcontext, Decimal
from datetime import datetime
from utils import json_view

@json_view
def pi(request):
    precision = 200

    #This took long time, for 10000 digits
    getcontext().prec = 500
    t1 = datetime.now()
    a = 1
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = 1
    pi = 0
    for x in range(0, precision):
        nextA = (a + b) / 2
        nextB = (a * b).sqrt()
        nextT = t - p * ((a - nextA) ** 2)
        nextP = 2 * p
        pi = ((a + b) ** 2) / (4 * t)
        a,b,t,p = nextA,nextB,nextT,nextP
    t2 = datetime.now()
    result = {
        'time': str(t2-t1),
        'pi': str(pi)
    }
    return result
