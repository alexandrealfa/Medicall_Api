from http import HTTPStatus
from . import BaseView


class Home(BaseView):
    def get(self):
        return {"message": "welcome to home Medicall"}, HTTPStatus.OK