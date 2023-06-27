import json

from settings import PATH_WITH_FIXTURES


def get_data(path):
    '''Чтение файла json'''
    with open(path) as file:
        data_list = json.load(file)
        return data_list


def get_valid_data(data_list):
    '''Удаление пустых словарей'''
    valid_data_list = []
    for operation in data_list:
        if operation:
            valid_data_list.append(operation)
    return valid_data_list


def convert_names(valid_data_list):
    '''Замена названий ключей'''
    operations_list = []
    for operation in valid_data_list:
        data = {}
        for key, value in operation.items():
            if key == 'id':
                data['pk'] = value
            elif key == 'operationAmount':
                data['operation_amount'] = value
            elif key == 'from':
                data['from_'] = value
            else:
                data[key] = value
        operations_list.append(data)
    return operations_list


def first_five_sorted_operations(operations_list):
    '''Получение последних пяти отсортированных операций'''
    return sorted(operations_list,
            key=lambda operations_list: (operations_list['state'], operations_list['date']),
            reverse=True)[:5]

five_operations = first_five_sorted_operations(convert_names(get_valid_data(get_data(PATH_WITH_FIXTURES))))