import time

def time_this(num_runs):
    def decorator_time_this(func):
        def wrap_time_this():
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return wrap_time_this
    return decorator_time_this

@time_this(num_runs=20)
def f():
    for j in range(1000000):
        pass

f()
