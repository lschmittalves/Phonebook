import json


class PhonebookRepository:
    objects = []

    def __init__(self):
        self.__load()

    def __load(self):
        with open("phonebook.json", "r") as read_file:
            self.objects = json.load(read_file)

    def __commit(self):
        with open("phonebook.json", "w+") as write_file:
            json.dump(self.objects, write_file)

    def get_by_phone(self, phone):
        return next(x for x in self.objects if x.phone == phone)

    def add(self, phonebook_item):
        self.objects.append(phonebook_item)
        self.__commit()
        return

    def edit(self, phonebook_item):
        existent_phone_item = next(x for x in self.objects if x is phonebook_item)
        existent_phone_item.name = phonebook_item.name
        self.__commit()
        return

    def delete(self, phone):
        self.objects[:] = [x for x in self.objects if x.phone != phone]
        self.__commit()
        return
