import timeit
import httplib2


# Hit the dynamic page 100 times, time the response time

def load_speed():
    t = timeit.Timer("h.request('https://wwauth.multiply.co.za',headers={'cache-control':'no-cache'})",
                     "from httplib2 import Http; h=Http()")
    times = t.repeat(20, 1)
    times = round(sum(times) / 20, 1)
    return times
