#!/usr/bin/python3
# -*- coding: utf-8 -*-
# импорты должны быть отсортированы и разбиты на общие и локальные


"""Общий docstring для файла"""


def verb_description(input_string: str = "вам", input_list: list = [0, 1]) -> dict:
    """
    ToDo: Что еще необходимо сделать для функции
    :param input_string:
    :param input_list:
    :return:
    """
    print(input_string)
    print(input_list)

    return dict


# My_example
# @staticmethod
# def read_config(path: str) -> dict:
#     """
#     Функция чтения конфигурационного файла. Для каждого бинарного файла в такой же директории
#     должен содержаться одноименный json, в котором хранятся конфигурационный данные
#     :param path: путь до входных данных
#     :return: json с конфигурационными данными
#     :raises FileNotFoundError: файла может не быть
#     :raises PermissionError: Нет прав доступа
#     :raises json.decoder.JSONDecodeError: Невалидный файл(ошибка в чтение json)
#     """
#     path = Path(path).resolve()  # Делает путь абсолютным
#     json_path = path.with_suffix(".json")  # изменяет формат bin на json
#     output_json = {}  # json с конфигурационными данными
#     try:
#         with open(json_path) as jsonfile:
#             config = json.load(jsonfile)
#             output_json = {k1: {int(k2): v2 for k2, v2 in v1.items()} for k1, v1 in
#                            config.items()} if config else {}
#             if output_json == {}:
#                 logger.critical(f"Invalid file (error in reading json) {json_path}")
#                 # raise json.decoder.JSONDecodeError("", "", "")
#             else:
#                 logger.info("successful reading of the configuration file")
#     except FileNotFoundError:
#         logger.critical(f"the file does not exist {json_path}")
#     except json.decoder.JSONDecodeError:
#         logger.critical(f"Invalid file (error in reading json) {json_path}")
#     except PermissionError:
#         logger.critical(f"file access error {json_path}")
#     finally:
#         return output_json


if __name__ == "__main__":
    verb_description()
