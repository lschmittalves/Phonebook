import json
import os


class PhonebookRepository:
    objects = []

    def __init__(self):
        self.__load()

    def __load(self):
        if not os.path.isfile('phonebook.json'):
            self.commit()

        with open("phonebook.json", "r") as read_file:
            self.objects = json.load(read_file)

    def commit(self):
        with open("phonebook.json", "w+") as write_file:
            json.dump(self.objects, write_file)

    def get_by_phone(self, phone):
        return next((x for x in self.objects if x['phone'] == phone), None)

    def add(self, phonebook_dict):
        self.objects.append(phonebook_dict)
        self.commit()
        return

    def delete(self, phone):
        self.objects[:] = [x for x in self.objects if x['phone'] != phone]
        self.commit()
        return
