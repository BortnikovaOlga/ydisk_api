from typing import Any

import cattr
from requests import Response

from src.api.common.tools import from_rus_to_lat


class BaseApi:

    def __init__(self, app):
        self.app = app

    def structure(self, response: Response, type_response, translate_map: dict = None) -> Response:
        """
        Try to structure response
        :param translate_map: map translate rus key to latin key in json
        :param response: response
        :param type_response: type response
        :return: modify response with "data" field
        """
        if type_response:
            try:
                response.data = cattr.structure(response.json() if not translate_map
                                                else from_rus_to_lat(response.json(), translate_map), type_response)
            except Exception as e:
                raise e
        return response

    def _post(self, url: str, data: Any, params=None, type_response=None, translate_map=None, header=None) -> Response:
        """
        Метод POST
        """
        if data is not None and not isinstance(data, (dict, list)):
            data = data.to_dict()
        response = self.app.client.request(method="POST",
                                           url=url,
                                           json=data,
                                           headers=header,
                                           params=params)

        return self.structure(response, type_response=type_response, translate_map=translate_map)

    def _get(self, url: str, type_response=None, translate_map=None, header=None, params=None) -> Response:
        """
        Метод GET
        """
        response = self.app.client.request(method="GET",
                                           url=url,
                                           headers=header,
                                           params=params)
        return self.structure(response, type_response=type_response, translate_map=translate_map)

    def _put(self, url: str, data: Any, type_response=None, header=None) -> Response:
        """
        Метод PUT
        """
        if data is not None and not isinstance(data, (dict, list)):
            data = data.to_dict()
        response = self.app.client.request(method="PUT",
                                           url=url,
                                           json=data,
                                           headers=header)
        return self.structure(response, type_response=type_response)

    def _delete(self, url: str, type_response=None, header=None) -> Response:
        """
        Метод DELETE
        """
        response = self.app.client.request(method="DELETE",
                                           url=url,
                                           headers=header)
        return self.structure(response, type_response=type_response)

    def _delete_with_key(self, url: str, key: dict, type_response=None, header=None):
        response = self.app.client.request(method="DELETE",
                                           url=url,
                                           json=key,
                                           headers=header)
        return self.structure(response, type_response=type_response)

    def _patch(self, url: str, data: Any, type_response=None) -> Response:
        """
        Метод PATCH
        """
        response = self.app.client.request(method="PATCH",
                                           url=url,
                                           json=data.to_dict() if data else {})
        return self.structure(response, type_response=type_response)
