
from src.api.base.client import Client
from src.api.disk_api.api import DiskApi


class Application:
    def __init__(self, url):
        self.url = url
        self.client = Client()
        self.disk_api = DiskApi(self)

    # def get_api(self, page_type: AppApis):
    #     return self.__api_factory.get_api(page_type)
