
import os

from users import User
from software import Software
from context import Context

from subclass import Singleton


class Tank(Singleton):

    def init_os(self):
        # self._notificator = Notificator()
        # self._notificator.setup()
        pass


    def init_software(self):
        self._software = Software()
        self._software.setup()
        self._software.print_header()

        self._user = User()
        self._user.setup()

        self._context = Context()
        self._context.setup()


    @property
    def software(self):
        return self._software

    @property
    def user(self):
        return self._user

    @property
    def context(self):
        return self._context
