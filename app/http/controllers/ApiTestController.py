"""A ApiTestController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class ApiTestController(Controller):
    """ApiTestController Controller Class."""

    def __init__(self, request: Request):
        """ApiTestController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return '123'
