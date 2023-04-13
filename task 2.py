'''
Реализовать работу со связным списком на языке Python. Создать два класса: Node
– элемент списка с атрибутами data (данные) и next (адрес следующего элемента
списка), а также класс List (список) c атрибутами head - адрес первого элемента
списка (первоначальное значение None) и length – длина списка (его необходимо
изменять при каждом добавлении и удалении элементов). Методы: append – добавить
элемент в конец списка, remove – удалить элемент с начала списка, out – вывести
список на экран, len – вывести длину списка. Реализовать меню пользователя для
работы со списком.
'''

class Node:
    def init(self, data):
        self.data = data
        self.next = None
class List:
    def init(self):
        self.head = None
        self.length = 0
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self_head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
        else:
            print("Лист пуст")
    def out(self):
        if self.head in None:
            print("Лист пуст")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end =" ")
                current_node = current_node.next
            print()
    def len(self):
        return self.length

def menu():
    my_list = List()
    while True:
        print("1. Добавить элемент в конец списка")
        print("2. Удалить элемент с начала списка")
        print("3. Вывести список на экран")
        print("4. Вывести длину списка")
        print("5. Выход")
        move = input("Выберите действие: ")
        if move == '1':
            data = input("Заполните список: ")
            my_list.append(data)
        elif move == '2':
            my_list.remove()
        elif move == '3':
            my_list.out()
        elif move == '4':
            print(len(my_list))
        elif move == '5':
            break
        else:
            print("Данные ошибочны")
            
if name == "main":
    menu()
