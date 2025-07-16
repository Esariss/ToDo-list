import os, json
from json import JSONDecodeError

class ToDo:
    data = None
    task = None
    choice = None
    todo_list = []

    def get_info(self):
        self.data = input("введите дату или время задачи: ")
        self.task = input("введите задачу: ")
        self.todo_list.append({
            "data": str(self.data),
            "task": str(self.task)
        })

    def info_to_json(self):
        with open("todo.json", "w", encoding="utf-8") as file:
            json.dump(self.todo_list, file , ensure_ascii=False, indent=4)

    def info_to_python(self):
        if os.path.exists("todo.json"):
            with open("todo.json", "r", encoding="utf-8") as file:
                self.todo_list = json.load(file)
        else:
            self.todo_list = []

        for index, el in enumerate(self.todo_list, start=1):
            print(f"{index}. Дата: {el['data']} | Задача: {el['task']}")

    def start_program(self):
        print("""
добро пожаловать в To-Do list
-----------------------------
выберите действие:
написать задачу(-1-)
посмотреть список задач(-2-)
завершить программу (-3- , stop , конец)
-----------------------------
        """)
        while True:
            try:
                self.choice = input("выберите действие:")

                if self.choice == "1":
                    self.get_info()
                    self.info_to_json()

                elif self.choice == "2":
                    self.info_to_python()

                elif self.choice == "3" or "stop" or "конец":
                    break
                else:
                    print("извините, запрос не был понят.\n пожалуйста повторите попытку")
            except JSONDecodeError:
                print("в списке пока нет задач")

test = ToDo()
test.start_program()
