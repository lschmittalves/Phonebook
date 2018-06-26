from cement.core.foundation import CementApp
from .controller import PhonebookShellController


class PhonebookApp(CementApp):
    class Meta:
        label = 'phonebookapp'
        base_controller = PhonebookShellController


with PhonebookApp() as app:
    app.run()
