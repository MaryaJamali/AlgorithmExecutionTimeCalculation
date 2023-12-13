import time


def get_time(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print("Runtime took {} seconds".format(round(t2 - t1, 2)))
        return f
    return inner


@get_time
def example():
    my_list = []
    for x in range(100000):
        if x > 10:
            my_list.append(x + 2)
    return "Algorithm Done"


print(example())
