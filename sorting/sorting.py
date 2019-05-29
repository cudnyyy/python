
from operator import attrgetter
#
# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# s_li = sorted(li, reverse=True)
#
# print('Sorted Variable: \t', s_li)
#
# li.sort()
#
# print('Original Variable: \t', li)
#
# tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# s_tup = sorted(tup)
#
# print('Tuple: \t\t\t\t', s_tup)
#
# di = {'name': 'Cudny', 'job': 'Graphic', 'age': None, 'os': 'Windows'}
# s_di = sorted(di)
# print('Dict: \t\t\t\t', s_di)
#
# li_2 = [-6, -5, -4, 1, 2, 3]
# s_li_2 = sorted(li_2, key=abs)
# print(s_li_2)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# s_employees = sorted(employees, key=lambda e: e.name)
s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)
