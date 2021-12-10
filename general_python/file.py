"""
    Gestion de archivos en python

"""
# import json
# PEP-8
from decimal import Decimal
from json import load as json_lectura

PATH_RESOURCES = "resources/demo.json"


class CustomException(Exception):
    pass


# try:
#     f = open(PATH_RESOURCES, "r")
#     data = json.load(f)
#     average_customers = []
#     for item in data.get("customers"):
#         average_customers.append(item)
#     result: dict = {"totalCustomers": len(average_customers)}
#     print(result)
# except Exception as e:
#     print("error: ", e)


def read_data_to_json(file_path: str) -> dict:
    """
    this function
    :param file_path:
    :return:
    """
    result: dict = {}
    try:
        f = open(PATH_RESOURCES, "r")
        data = json_lectura(f)
        result["totalCustomers"] = len(data.get("customers"))
        return result
    except Exception as e:
        print("error: ", e)
        return None


class BaseInfo:
    dni: str
    name: str
    salary: Decimal
    __phone: str

    def __init__(self):  # constructor
        self.__phone = ""

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if value != "":
            self.__phone = value
        else:
            print("Error")


class Profile:
    area: str

    def display_name(self):
        print("desde profile")


class Customer(BaseInfo, Profile):
    pass

    def display_name(self):
        super().display_name()


c = Customer()
print(c.phone)
c.phone = "99999999"
print(c.phone)
