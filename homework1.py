class Calculator():
    def add(self, num1, num2):
            result = num1 + num2
            print(num1, '+', num2, "=", result)
    def suntract(self, num1, num2):
        result = num1 - num2
        print(num1, '-', num2, "=", result)
    def multiply(self, num1, num2):
        result = num1 * num2
        print(num1, '*', num2, "=", result)
    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
        else:
            return "Деление на 0 невозможно"
        print(num1, '/', num2, "=", result)



calculator = Calculator()
calculator.add(20, 100)


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

some = TodoList()
some.add_task("Сделать дз")
some.add_task("Убрать дом")
some.show_tasks()
some.remove_task("Сделать дз")
some.show_tasks()