from cement.core.controller import CementBaseController, expose
from repository import PhonebookRepository
from models import PhoneBookItem


class PhonebookShellController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Simple Phonebook"
        arguments = [
            (['-n', '--name'],
             dict(action='store', help='Name')),
            (['-p', '--phone'],
             dict(action='store', help='Phone')),
        ]

    __repository = {}

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__repository = PhonebookRepository()

    @expose(hide=True)
    def default(self):
        self.list()

    @expose(aliases=['f'], help="This command find a existent item to the phonebook by phone")
    def edit(self):
        phonebook_item = self.__repository.get_by_phone(self.app.pargs.phone)

        if not phonebook_item:
            self.app.log.info(f'Item with phone number {self.app.pargs.phone} was not found')
            return

        self.app.log.info(f'Name: {phonebook_item.name} Phone: {phonebook_item.phone}')

    @expose(aliases=['a'], help="This command add a new item to the phonebook")
    def add(self):
        if not self.app.pargs.name:
            self.app.log.warning("Provide the --name parameter")
        if not self.app.pargs.phone:
            self.app.log.warning("Provide the --phone parameter")

        phonebook_item = PhoneBookItem(self.app.pargs.name, self.app.pargs.phone)

        self.__repository.add(phonebook_item)

        self.app.log.info(f'Item with phone number {self.app.pargs.phone} was add')

    @expose(aliases=['e'], help="This command edit a existent item to the phonebook by phone")
    def edit(self):
        phonebook_item = self.__repository.get_by_phone(self.app.pargs.phone)

        if not phonebook_item:
            self.app.log.info(f'Item with phone number {self.app.pargs.phone} was not found')
            return

        phonebook_item.name = self.app.pargs.name

        self.app.log.info(f'Item with phone number {self.app.pargs.phone} was update')

    @expose(aliases=['d'], help="This command delete a existent item to the phonebook by phone")
    def delete(self):
        self.__repository.delete(self.app.pargs.phone)
        self.app.log.info(f'Item with phone number {self.app.pargs.phone} was remove')

    @expose(aliases=['l'], help="This command list the existents itens of the phonebook")
    def list(self):
        for phonebook_item in self.__repository.objects:
            self.app.log.info(f'Name: {phonebook_item.name} Phone: {phonebook_item.phone}')



