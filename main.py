from src.data import five_operations
from src.operation import Operation


def get_operations(five_operations):
    '''Создание списка экземпляров класса Operation'''
    list_with_operations = []
    for i in five_operations:
        list_with_operations.append(Operation(**i))
    return list_with_operations


def main(operations):
    for operation in operations:
        print(operation)
        print()

if __name__ == '__main__':
    main(get_operations(five_operations))