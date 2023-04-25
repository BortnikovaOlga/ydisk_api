from urllib.parse import urlencode

from src.api.base.base_api import BaseApi
from src.api.common.deco import logging as log


class DiskApi(BaseApi):

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.url = f"{self.app.url}{self.ENDPOINT_URL}"

    ENDPOINT_URL = "/v1/disk"

    @log("USER DISK INFO")
    def get_user_disk_info(self, type_response=None, header=None):
        return self._get(self.url, type_response=type_response, header=header)

    @log("CREATE DIR")
    def create_dir(self, path, type_response=None, header=None):
        return self._put(f"{self.url}/resources?{urlencode({'path': path})}",
                         data=None,
                         type_response=type_response,
                         header=header)

    @log("DELETE FILE OR DIR")
    def delete_file_or_dir(self, path, permanently='false', type_response=None, header=None):
        params = {"path": path, "permanently": permanently}
        return self._delete(f"{self.url}/resources?{urlencode(params)}",
                            type_response=type_response,
                            header=header)

    @log("COPY FILE OR DIR")
    def copy_file_or_dir(self, from_path, to_path, overwrite='false', type_response=None, header=None):
        params = {"from": from_path, "path": to_path, "overwrite": overwrite}
        return self._post(f"{self.url}/resources/copy?{urlencode(params)}",
                          data=None,
                          type_response=type_response,
                          header=header)

    @log("MOVE FILE OR DIR")
    def move_file_or_dir(self, from_path, to_path, overwrite='false', type_response=None, header=None):
        params = {"from": from_path, "path": to_path, "overwrite": overwrite}
        return self._post(f"{self.url}/resources/move?{urlencode(params)}",
                          data=None,
                          type_response=type_response,
                          header=header)
