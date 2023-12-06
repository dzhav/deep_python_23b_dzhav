class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        n_dict = {}
        for key, value in dct.items():
            if key.startswith("__") and key.endswith("__"):
                n_dict.update({key: value})
            else:
                n_dict.update({"custom_" + key: value})

        n_dict['__setattr__'] = cls.custom_setattr
        return super().__new__(cls, name, bases, n_dict)

    @staticmethod
    def custom_setattr(inst, name, value):
        if name.startswith("__") or name.startswith("custom_"):
            super(type(inst), inst).__setattr__(name, value)
        else:
            inst.__dict__.update({"custom_" + name: value})


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.custom_val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


assert CustomClass.custom_x == 50

try:
    CustomClass.x
except AttributeError:
    print("type object 'CustomClass' has no attribute 'x'")

inst = CustomClass()
assert inst.custom_x == 50
assert inst.custom_val == 99
assert inst.custom_line() == 100
assert str(inst) == "Custom_by_metaclass"

try:
    inst.x
except AttributeError:
    print("'CustomClass' object has no attribute 'x'")

try:
    inst.val
except AttributeError:
    print("'CustomClass' object has no attribute 'val'")

try:
    inst.line()
except AttributeError:
    print("'CustomClass' object has no attribute 'line'")

try:
    inst.yyy
except AttributeError:
    print("'CustomClass' object has no attribute 'yyy'")

inst.dynamic = "added later"
assert inst.custom_dynamic == "added later"

try:
    inst.dynamic
except AttributeError:
    print("'CustomClass' object has no attribute 'dynamic'")

# Вывод
# type object 'CustomClass' has no attribute 'x'
# 'CustomClass' object has no attribute 'x'
# 'CustomClass' object has no attribute 'val'
# 'CustomClass' object has no attribute 'line'
# 'CustomClass' object has no attribute 'yyy'
# 'CustomClass' object has no attribute 'dynamic'
