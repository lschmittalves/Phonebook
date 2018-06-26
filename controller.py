from cement.core.controller import CementBaseController, expose


class PhonebookShellController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Simple Phonebook"
        arguments = [
            (['-n', '--name'],
             dict(action='store', help='Name')),
            (['-t', '--tel'],
             dict(action='store', help='Telephone')),
        ]

    @expose(hide=True)
    def default(self):
        self.list()

    @expose(aliases=['a'], help="This command add a new item to the phonebook")
    def add(self):
        self.app.log.info("Inside add")

    @expose(aliases=['e'], help="This command edit a existent item to the phonebook by phone")
    def edit(self):
        self.app.log.info("Inside edit")

    @expose(aliases=['d'], help="This command delete a existent item to the phonebook by phone")
    def delete(self):
        self.app.log.info("Inside delete")

    @expose(aliases=['l'], help="This command list the existents itens of the phonebook")
    def list(self):
        self.app.log.info("Inside list")
