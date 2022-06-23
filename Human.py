import json
from json2xml import json2xml
from json2xml.utils import readfromstring

class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        self = json.dumps(self.__dict__)

        print(self)

    def convert_to_xml(self):
        self = json.dumps(self.__dict__)
        data = readfromstring(self)

        print(json2xml.Json2xml(data).to_xml())

    def user_input(self):
        user_choice = input("Enter json or xml: ")
        if user_choice == 'json':
            return h.convert_to_json()

        if user_choice == 'xml':
            return h.convert_to_xml()

        else:
            print('wrong answer')

h = Human('Alessandro', 22, 'male', 2000)

h.user_input()




