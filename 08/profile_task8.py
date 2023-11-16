import time
import weakref


n = 500_000


def profiling_code():
    class RegularClass:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    class SlottedClass:
        __slots__ = ['a', 'b', 'c', 'd']
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    class WeakRefClass:
        def __init__(self, a, b, c, d):
            self.a = weakref.ref(a)
            self.b = weakref.ref(b)
            self.c = weakref.ref(c)
            self.d = weakref.ref(d)

    class CustomClass:
        def __init__(self, value):
            self.value = value

    start_time = time.time()
    ordinary_instances = [RegularClass(CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(4)) for _ in range(n)]
    print("Время создания экземпляров класса OrdinaryClass:", time.time() - start_time)

    start_time = time.time()
    slotted_instances = [SlottedClass(CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(4)) for _ in range(n)]
    print("Время создания экземпляров класса SlottedClass:", time.time() - start_time)

    start_time = time.time()
    weakref_instances = [WeakRefClass(CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(4)) for _ in range(n)]
    print("Время создания экземпляров класса WeakRefClass:", time.time() - start_time)

    start_time = time.time()
    for instance in ordinary_instances:
        instance.a
        instance.b
        instance.c
        instance.d
    print("Время чтения атрибутов класса OrdinaryClass:", time.time() - start_time)

    start_time = time.time()
    for instance in slotted_instances:
        instance.a
        instance.b
        instance.c
        instance.d
    print("Время чтения атрибутов класса SlottedClass:", time.time() - start_time)

    start_time = time.time()
    for instance in weakref_instances:
        instance.a()
        instance.b()
        instance.c()
        instance.d()
    print("Время чтения атрибутов класса WeakRefClass:", time.time() - start_time)

    start_time = time.time()
    for instance in ordinary_instances:
        instance.a = CustomClass(4)
        instance.b = CustomClass(3)
        instance.c = CustomClass(2)
        instance.d = CustomClass(1)
    print("Время изменения атрибутов класса OrdinaryClass:", time.time() - start_time)

    start_time = time.time()
    for instance in slotted_instances:
        instance.a = CustomClass(4)
        instance.b = CustomClass(3)
        instance.c = CustomClass(2)
        instance.d = CustomClass(1)
    print("Время изменения атрибутов класса SlottedClass:", time.time() - start_time)

    start_time = time.time()
    for instance in weakref_instances:
        instance.a = CustomClass(4)
        instance.b = CustomClass(3)
        instance.c = CustomClass(2)
        instance.d = CustomClass(1)
    print("Время изменения атрибутов класса WeakRefClass:", time.time() - start_time)


# cProfile.run("profiling_code()", sort="cumulative")
if __name__ == "__main__":
    profiling_code()
