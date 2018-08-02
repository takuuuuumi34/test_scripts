class Employee(object):
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
        self.observers = set()

    def set_salary(self, new_salary):
        self.salary = new_salary
        for observer in self.observers:
            observer(self)

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)


class Payroll(object):
    def update(self, changed_employee):
        print("changed {}".format(changed_employee.name))
        print("current salary is {}, role is {}".format(changed_employee.salary, changed_employee.title))


class Taxman(object):
    def update(self, changed_employee):
        print("billing to {}".format(changed_employee.name))


if __name__ == "__main__":
    payroll = Payroll()
    taxman = Taxman()
    fred = Employee("fred", "engeneer", 300*10000)
    fred.add_observer(payroll.update)
    fred.add_observer(taxman.update)
    fred.set_salary(350*10000)
    print()
    fred.remove_observer(taxman.update)
    fred.set_salary(400*10000)
