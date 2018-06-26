from .models import PhoneBookItem
import json


class PhonebookRepository:
    objects = []

    def __load(self):
        with open("phonebook.json", "r") as read_file:
            self.objects = json.load(read_file)

    def __commit(self):
        with open("phonebook.json", "w+") as write_file:
            json.dump(self.objects, write_file)

    def add(self, phonebook_item):
        self.__load()
        self.objects.append(phonebook_item)
        self.__commit()
        return

    def edit(self, phonebook_item):
        self.__load()
        phone_item = next(for x in self.objects if x.phone == phonebook_item.phone)
        self.__commit()
        return

    def delete(self, phone):
        self.__load()
        self.objects[:] = [x for x in self.objects if x.phone != phone]
        self.__commit()
        return
